"""
controller.py  —  Topside
Reads Xbox 360 controller via pygame, sends JSON to Jetson over TCP.

Message format (sent every loop tick):
{
  "throttle": int,   # 1150–1850 (vertical)
  "yaw":      int,   # 1150–1850
  "forward":  int,   # 1150–1850
  "lateral":  int,   # 1150–1850
  "gripper_a": 0|1,
  "gripper_b": 0|1,
  "arm":       bool | None,   # FIX: None every tick EXCEPT the tick the button was pressed
  "mode":      "manual"|"stabilize"|"depth_hold"|None
}

Controller layout:
  Left stick  up/down   → forward / backward
  Left stick  left/right→ lateral
  Right stick up/down   → throttle (vertical)
  Right stick left/right→ yaw
  LB          → gain down  (100→75→50→25→10)
  RB          → gain up    (10→25→50→75→100)
  BACK        → arm / disarm toggle
  D-pad click → stabilize mode  (click again → manual)
  A           → toggle gripper A (A2 MOSFET)
  B           → toggle gripper B (A3 MOSFET)
"""

import pygame
import socket
import json
import time
import platform

JETSON_IP   = "192.168.33.1"
JETSON_PORT = 5555
LOOP_HZ     = 100

GAIN_STEPS  = [10, 25, 50, 75, 100]

# PWM limits
PWM_CENTER  = 1500
PWM_SINGLE  = 350   # ±range when moving one axis only
PWM_COMBINED= 250   # ±range when mixing axes (prevents thruster overload)
DEADZONE    = 0.08


def clamp(val, lo, hi):
    return max(lo, min(hi, val))


def axes_to_pwm(raw, gain_pct, combined: bool):
    """Map joystick raw [-1,1] to PWM delta, respecting single/combined limits."""
    limit = PWM_COMBINED if combined else PWM_SINGLE
    scaled = raw * limit * (gain_pct / 100.0)
    return int(clamp(scaled, -limit, limit))


class Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()

        self._joy = None
        self._gain_idx = 4          # start at 100%
        self._gripper_a = 0
        self._gripper_b = 0
        self._armed = False
        self._mode = "manual"       # "manual" | "stabilize" | "depth_hold"

        # button edge-detection state
        self._prev_buttons = {}
        self._prev_hat = (0, 0)

        self._os = platform.system()

        # axis indices differ between Linux and Windows for the Xbox 360 controller
        if self._os == "Linux":
            self.AX_LH = 0   # left horizontal
            self.AX_LV = 1   # left vertical
            self.AX_RH = 3   # right horizontal
            self.AX_RV = 4   # right vertical
        else:  # Windows
            self.AX_LH = 0
            self.AX_LV = 1
            self.AX_RH = 2
            self.AX_RV = 3

        # button indices (Xbox 360, same on both OS via pygame)
        self.BTN_A    = 0
        self.BTN_B    = 1
        self.BTN_X    = 2
        self.BTN_Y    = 3
        self.BTN_LB   = 4
        self.BTN_RB   = 5
        self.BTN_BACK = 6
        self.BTN_START= 7
        self.BTN_LT = 8   # L2 (as button)
        self.BTN_RT = 9   # R2 (as button)

        self._num_cameras = 3   # cameras 1–3
        self._camera_idx  = 0

    # ------------------------------------------------------------------ #
    #  Connection helpers                                                  #
    # ------------------------------------------------------------------ #
    def _connect_joystick(self):
        count = pygame.joystick.get_count()
        if count == 0:
            return False
        joy = pygame.joystick.Joystick(0)
        joy.init()
        name = joy.get_name()
        if "Xbox 360" not in name and "Xbox360" not in name:
            print(f"[CTRL] Unrecognised controller: {name}. Please use Xbox 360.")
            joy.quit()
            return False
        self._joy = joy
        print(f"[CTRL] Connected: {name}")
        return True

    # ------------------------------------------------------------------ #
    #  Button helpers (rising-edge only)                                  #
    # ------------------------------------------------------------------ #
    def _pressed(self, btn_id: int) -> bool:
        cur  = self._joy.get_button(btn_id)
        prev = self._prev_buttons.get(btn_id, 0)
        return cur == 1 and prev == 0

    def _update_prev_buttons(self):
        for i in range(self._joy.get_numbuttons()):
            self._prev_buttons[i] = self._joy.get_button(i)

    # ------------------------------------------------------------------ #
    #  Axis helpers                                                        #
    # ------------------------------------------------------------------ #
    def _axis(self, idx: int) -> float:
        raw = self._joy.get_axis(idx)
        return raw if abs(raw) > DEADZONE else 0.0

    # ------------------------------------------------------------------ #
    #  Build message                                                       #
    # ------------------------------------------------------------------ #
    def read(self):
        pygame.event.pump()
        # reconnect if disconnected
        if self._joy is None:
            if pygame.joystick.get_count() == 0:
                return None
            self._connect_joystick()
            return None
        # check if still connected
        if pygame.joystick.get_count() == 0:
            print("[CTRL] Joystick disconnected.")
            self._joy = None
            self._prev_buttons = {}
            self._prev_hat = (0, 0)
            return None

        gain = GAIN_STEPS[self._gain_idx]

        # --- axes ---
        lh = self._axis(self.AX_LH)   # lateral
        lv = self._axis(self.AX_LV)   # forward  (inverted: up = negative)
        rh = self._axis(self.AX_RH)   # yaw
        rv = self._axis(self.AX_RV)   # throttle (inverted: up = negative)

        # detect combined movement (any two axes active simultaneously)
        moving_horizontal = (lh != 0 or lv != 0)
        moving_vertical   = (rv != 0)
        combined = moving_horizontal and moving_vertical

        lateral   = PWM_CENTER + axes_to_pwm( lh,  gain, combined)
        forward   = PWM_CENTER + axes_to_pwm(-lv,  gain, combined)   # invert
        yaw       = PWM_CENTER + axes_to_pwm( rh,  gain, combined)
        throttle  = PWM_CENTER + axes_to_pwm(-rv,  gain, combined)   # invert

        # --- button events ---
        mode_cmd = None
        arm_cmd  = None      # FIX: None by default — only set on the press tick

        if self._pressed(self.BTN_A):
            self._gripper_a ^= 1
            print(f"[CTRL] Gripper A → {self._gripper_a}")

        if self._pressed(self.BTN_B):
            self._gripper_b ^= 1
            print(f"[CTRL] Gripper B → {self._gripper_b}")

        if self._pressed(self.BTN_LB):
            self._gain_idx = max(0, self._gain_idx - 1)
            print(f"[CTRL] Gain → {GAIN_STEPS[self._gain_idx]}%")

        if self._pressed(self.BTN_RB):
            self._gain_idx = min(len(GAIN_STEPS) - 1, self._gain_idx + 1)
            print(f"[CTRL] Gain → {GAIN_STEPS[self._gain_idx]}%")

        if self._pressed(self.BTN_BACK):
            self._armed = not self._armed
            arm_cmd = self._armed    # FIX: only emitted THIS tick, None all other ticks
            print(f"[CTRL] {'ARM' if self._armed else 'DISARM'}")

        camera_cmd = None

        if self._pressed(self.BTN_LT):
            self._camera_idx = (self._camera_idx - 1) % self._num_cameras
            camera_cmd = self._camera_idx
            print(f"[CTRL] Camera slot 0 → cam {self._camera_idx + 1}")

        if self._pressed(self.BTN_RT):
            self._camera_idx = (self._camera_idx + 1) % self._num_cameras
            camera_cmd = self._camera_idx
            print(f"[CTRL] Camera slot 0 → cam {self._camera_idx + 1}")

        # D-pad: any direction pressed = toggle stabilize / manual
        hat = self._joy.get_hat(0)
        if hat != (0, 0) and self._prev_hat == (0, 0):
            if self._mode == "manual":
                self._mode = "stabilize"
            else:
                self._mode = "manual"
            mode_cmd = self._mode
            print(f"[CTRL] Mode → {self._mode}")
        self._prev_hat = hat

        self._update_prev_buttons()

        return {
            "throttle":  throttle,
            "yaw":       yaw,
            "forward":   forward,
            "lateral":   lateral,
            "gripper_a": self._gripper_a,
            "gripper_b": self._gripper_b,
            "arm":       arm_cmd,    # FIX: None unless BACK was pressed this tick
            "mode":      mode_cmd,   # None unless changed this tick
            "gain":      gain,

            "camera": camera_cmd, 

            "left_x":  lh,
            "left_y":  lv,
            "right_x": rh,
            "right_y": rv,
        }

    # ------------------------------------------------------------------ #
    #  Public connect helper (library mode)                               #
    # ------------------------------------------------------------------ #
    def connect(self):
        """Initialize joystick for use in library mode (called by main.py)."""
        print("[CTRL] Waiting for Xbox 360 controller...")
        while self._joy is None:
            pygame.event.pump()
            if not self._connect_joystick():
                time.sleep(0.5)
        print("[CTRL] Controller ready.")

    # ------------------------------------------------------------------ #
    #  Main loop                                                           #
    # ------------------------------------------------------------------ #
    def run(self):
        sock = None
        dt = 1.0 / LOOP_HZ

        print(f"[CTRL] Connecting to Jetson {JETSON_IP}:{JETSON_PORT} ...")

        while True:
            # --- TCP connection ---
            while sock is None:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect((JETSON_IP, JETSON_PORT))
                    print("[CTRL] TCP connected to Jetson.")
                except OSError as e:
                    print(f"[CTRL] TCP error: {e}. Retrying in 1s...")
                    sock = None
                    time.sleep(1.0)

            # --- joystick connection ---
            while self._joy is None:
                if not self._connect_joystick():
                    time.sleep(0.5)
                    pygame.event.pump()

            # --- main loop ---
            try:
                while True:
                    t0 = time.time()

                    # check joystick still present
                    pygame.event.pump()
                    if pygame.joystick.get_count() == 0:
                        print("[CTRL] Joystick disconnected.")
                        self._joy = None
                        self._prev_buttons = {}
                        self._prev_hat = (0, 0)
                        break

                    msg = self.read()
                    if msg:
                        payload = (json.dumps(msg) + "\n").encode()
                        sock.sendall(payload)

                    elapsed = time.time() - t0
                    time.sleep(max(0.0, dt - elapsed))

            except (BrokenPipeError, ConnectionResetError, OSError) as e:
                print(f"[CTRL] TCP lost: {e}. Reconnecting...")
                try:
                    sock.close()
                except Exception:
                    pass
                sock = None

    def stop(self):
        pygame.joystick.quit()
        pygame.quit()


if __name__ == "__main__":
    ctrl = Controller()
    try:
        ctrl.run()
    except KeyboardInterrupt:
        print("\n[CTRL] Stopping.")
        ctrl.stop()