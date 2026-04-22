"""
jetson_gripper.py  —  Laptop (Topside)
Maintains a TCP connection to the Jetson and forwards gripper state.
Runs in its own background thread; auto-reconnects on drop.

Message sent to Jetson:
  {"gripper_a": 0|1, "gripper_b": 0|1}\n
"""

import threading
import socket
import json
import time

JETSON_IP   = "192.168.33.1"
JETSON_PORT = 5555
SEND_HZ     = 10   # 10×/s is plenty for gripper state


class JetsonGripperClient:
    def __init__(self):
        self._lock      = threading.Lock()
        self._running   = False
        self._gripper_a = 0
        self._gripper_b = 0

    # ------------------------------------------------------------------ #
    #  Called from main thread                                            #
    # ------------------------------------------------------------------ #
    def update(self, gripper_a: int, gripper_b: int):
        with self._lock:
            self._gripper_a = gripper_a
            self._gripper_b = gripper_b

    # ------------------------------------------------------------------ #
    #  Background thread                                                  #
    # ------------------------------------------------------------------ #
    def run(self):
        self._running = True
        dt = 1.0 / SEND_HZ

        while self._running:
            sock = None

            # --- connect ---
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5.0)
                sock.connect((JETSON_IP, JETSON_PORT))
                sock.settimeout(None)
                print(f"[GRIPPER] Connected to Jetson {JETSON_IP}:{JETSON_PORT}")
            except OSError as e:
                print(f"[GRIPPER] TCP connect failed: {e}. Retrying in 2s...")
                if sock:
                    try:
                        sock.close()
                    except Exception:
                        pass
                time.sleep(2.0)
                continue

            # --- send loop ---
            try:
                while self._running:
                    t0 = time.time()

                    with self._lock:
                        state = {
                            "gripper_a": self._gripper_a,
                            "gripper_b": self._gripper_b,
                        }
                    payload = (json.dumps(state) + "\n").encode()
                    sock.sendall(payload)

                    elapsed = time.time() - t0
                    time.sleep(max(0.0, dt - elapsed))

            except (BrokenPipeError, ConnectionResetError, OSError) as e:
                print(f"[GRIPPER] TCP lost: {e}. Reconnecting...")
            finally:
                try:
                    sock.close()
                except Exception:
                    pass

    def stop(self):
        self._running = False
