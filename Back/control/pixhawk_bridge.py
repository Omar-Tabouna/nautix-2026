"""
pixhawk_bridge.py — Laptop (Topside)
Connects to Pixhawk via MAVLink UDP through mavp2p running on the Jetson.
Runs in its own background thread.

Laptop --UDP-14550--> Jetson (mavp2p) --serial--> Pixhawk
"""

import threading
import time
from pymavlink import mavutil

MAVLINK_URI = "udp:192.168.33.2:14550"
PWM_MIN     = 1150
PWM_MAX     = 1850
PWM_CENTER  = 1500

def clamp_pwm(val: int) -> int:
    return max(PWM_MIN, min(PWM_MAX, val))


class PixhawkBridge:
    def __init__(self):
        self.__running        = False
        self.__throttle_value = PWM_CENTER
        self.__yaw_value      = PWM_CENTER
        self.__forward_value  = PWM_CENTER
        self.__lateral_value  = PWM_CENTER
        self.__armed          = False
        self.__last_time_seen = 0
        self.__connected      = False
        self.__pixhawk        = None
        self.sent_armed       = False
        self.sent_mode        = ""

    def update(self, throttle, yaw, forward, lateral, arm, mode):
        self.__throttle_value = clamp_pwm(throttle)
        self.__yaw_value      = clamp_pwm(yaw)
        self.__forward_value  = clamp_pwm(forward)
        self.__lateral_value  = clamp_pwm(lateral)

        if arm is not None:
            self.control_arm_disarm(arm)

        if mode is not None:
            if mode == "manual":
                self.control_manual_mode()
            elif mode == "stabilize":
                self.control_stabilize_mode()
            elif mode == "depth_hold":
                self.control_depth_hold_mode()

    def control_arm_disarm(self, arm: bool):
        if self.__pixhawk is None:
            return
        if arm:
            self.__pixhawk.arducopter_arm()
        else:
            self.__pixhawk.arducopter_disarm()

    def control_manual_mode(self):
        if self.__pixhawk is None:
            return
        mode_id = self.__pixhawk.mode_mapping()['MANUAL']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def control_stabilize_mode(self):
        if self.__pixhawk is None:
            return
        mode_id = self.__pixhawk.mode_mapping()['STABILIZE']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def control_depth_hold_mode(self):
        if self.__pixhawk is None:
            return
        mode_id = self.__pixhawk.mode_mapping()['ALT_HOLD']
        self.__pixhawk.mav.set_mode_send(
            self.__pixhawk.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)

    def run(self):
        self.__running = True
        while self.__running:
            try:
                self.__pixhawk = mavutil.mavlink_connection(MAVLINK_URI, autoreconnect=True, source_system=1)
                print("Waiting to connect to the pixhawk...")
                self.__pixhawk.wait_heartbeat()
            except OSError:
                continue
            print("Got a heartbeat")
            self.__last_time_seen = time.time()
            while self.__running:
                msg = self.__pixhawk.recv_match()
                if msg:
                    if msg.get_type() == 'HEARTBEAT':
                        if self.__connected == False:
                            self.__connected = True
                            print("connected to pixhawk")

                        self.__armed = self.__pixhawk.motors_armed()
                        if self.__armed != self.sent_armed:
                            self.sent_armed = self.__armed
                            if self.__armed != 0: print("armed")
                            else: print("disarmed")

                        self.mode = mavutil.mode_string_v10(msg)
                        if self.mode == "Mode(0x00000000)": self.mode = self.sent_mode
                        if self.mode != self.sent_mode:
                            self.sent_mode = self.mode
                            if self.mode == "MANUAL": print("manual mode")
                            elif self.mode == "STABILIZE": print("stabilize")
                            elif self.mode == "ALT_HOLD": print("depth hold")
                        self.__last_time_seen = time.time()
                if time.time() - self.__last_time_seen > 1.5:
                    if self.__connected:
                        self.__connected = False
                        self.sent_mode = ""
                        print("Disconnected, trying to reconnect to the pixhawk...")

    def move_rov(self):
        if self.__armed and self.__connected:
            rc_channel_values = [1500, 1500, self.__throttle_value, self.__yaw_value, self.__forward_value, self.__lateral_value, 65535, 65535, 65535]
            self.__pixhawk.mav.rc_channels_override_send(
                self.__pixhawk.target_system,
                self.__pixhawk.target_component,
                *rc_channel_values)

    def stop(self):
        if self.__connected:
            self.__connected = False
            self.control_arm_disarm(False)
            self.__pixhawk.close()
        self.__running = False