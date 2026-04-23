"""
main.py  —  Laptop (Topside)
Reads Xbox 360 controller, sends RC overrides directly to Pixhawk via MAVLink,
and forwards gripper state to the Jetson over TCP.

Architecture:
  Laptop → Pixhawk   : MAVLink UDP (via mavp2p already running on Jetson)
  Laptop → Jetson TCP: gripper JSON only  {"gripper_a": 0|1, "gripper_b": 0|1}

Run:
  python3 main.py
"""

import threading
import time
from PySide6.QtCore import QThread, Signal
from control.controller     import Controller
from control.pixhawk_bridge import PixhawkBridge
from control.jetson_gripper import JetsonGripperClient

LOOP_HZ = 200


class control_main(QThread):
    new_data = Signal(dict)

    def __init__(self):
        super().__init__()
        self._running = True

    def run(self):
        ctrl   = Controller()
        ctrl.connect()

        pix    = PixhawkBridge()
        jetson = JetsonGripperClient()

        pix_thread    = threading.Thread(target=pix.run,    daemon=True)
        jetson_thread = threading.Thread(target=jetson.run, daemon=True)
        pix_thread.start()
        jetson_thread.start()

        dt = 1.0 / LOOP_HZ  # 200Hz, matches joystick_class tick rate
        print("[MAIN] Running. Ctrl+C to stop.")

        try:
            while self._running:
                t0 = time.time()

                msg = ctrl.read()
                if msg:
                    self.new_data.emit(msg) 
                    pix.update(
                        throttle = msg["throttle"],
                        yaw      = msg["yaw"],
                        forward  = msg["forward"],
                        lateral  = msg["lateral"],
                        arm      = msg["arm"],
                        mode     = msg["mode"],
                    )

                    jetson.update(
                        gripper_a = msg["gripper_a"],
                        gripper_b = msg["gripper_b"],
                    )

                pix.move_rov()

                elapsed = time.time() - t0
                time.sleep(max(0.0, dt - elapsed))

        except KeyboardInterrupt:
            print("\n[MAIN] Stopping.")
        finally:
            pix.stop()
            jetson.stop()
            ctrl.stop()

    def stop(self):
        self._running = False
        self.quit()
        self.wait()


# if __name__ == "__main__":
#     control_main()