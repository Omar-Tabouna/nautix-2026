"""
jetson_gripper_server.py — Jetson NX (the ONLY file needed on the Jetson)

Accepts a TCP connection from the laptop and forwards gripper state to the
Arduino over serial.

Laptop --TCP 5555--> Jetson --serial 9600--> Arduino --GPIO--> MOSFETs

Message received from laptop:
 {"gripper_a": 0|1, "gripper_b": 0|1}\n

Message forwarded to Arduino:
 {"A2": 0|1, "A3": 0|1}\n

Run:
 python3 jetson_gripper_server.py
"""

import socket
import serial
import serial.tools.list_ports
import json
import threading
import time
import glob

LISTEN_HOST = "0.0.0.0"
LISTEN_PORT = 5555
BAUD_RATE = 9600
SEND_HZ = 10


# ------------------------------------------------------------------ #
# Serial helpers
# ------------------------------------------------------------------ #
def find_arduino_port():
    """Return first ttyUSB* or ttyACM* port found."""
    candidates = glob.glob("/dev/ttyUSB*") + glob.glob("/dev/ttyACM*")
    return candidates[0] if candidates else None


# ------------------------------------------------------------------ #
# Arduino serial writer thread
# ------------------------------------------------------------------ #
class ArduinoWriter:
    def __init__(self):
        self._lock = threading.Lock()
        self._running = False
        self._gripper_a = 0
        self._gripper_b = 0

    def update(self, gripper_a: int, gripper_b: int):
        with self._lock:
            self._gripper_a = gripper_a
            self._gripper_b = gripper_b

    def run(self):
        self._running = True
        ser = None
        dt = 1.0 / SEND_HZ

        while self._running:
            # --- find and open port ---
            if ser is None:
                port = find_arduino_port()
                if port is None:
                    print("[ARD] No Arduino found. Retrying in 2s...")
                    time.sleep(2.0)
                    continue

                try:
                    ser = serial.Serial(port, BAUD_RATE, timeout=1)
                    time.sleep(2.0)  # wait for Arduino reset after serial open
                    print(f"[ARD] Connected to Arduino on {port}")
                except serial.SerialException as e:
                    print(f"[ARD] Serial open failed: {e}")
                    ser = None
                    time.sleep(2.0)
                    continue

            # --- write state ---
            try:
                with self._lock:
                    payload = json.dumps({
                        "A2": self._gripper_a,
                        "A3": self._gripper_b
                    }) + "\n"

                ser.write(payload.encode())

            except serial.SerialException as e:
                print(f"[ARD] Write failed: {e}. Reconnecting...")
                try:
                    ser.close()
                except Exception:
                    pass

                ser = None
                time.sleep(dt)
                continue

            time.sleep(dt)

        if ser:
            try:
                ser.close()
            except Exception:
                pass

    def stop(self):
        self._running = False


# ------------------------------------------------------------------ #
# TCP client handler
# ------------------------------------------------------------------ #
def handle_client(conn, addr, arduino: ArduinoWriter):
    print(f"[TCP] Laptop connected from {addr}")
    buf = ""

    try:
        while True:
            data = conn.recv(1024).decode(errors="ignore")
            if not data:
                break

            buf += data

            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                line = line.strip()

                if not line:
                    continue

                try:
                    msg = json.loads(line)
                except json.JSONDecodeError:
                    print(f"[TCP] Bad JSON: {line}")
                    continue

                arduino.update(
                    gripper_a=int(msg.get("gripper_a", 0)),
                    gripper_b=int(msg.get("gripper_b", 0)),
                )

    except (ConnectionResetError, OSError) as e:
        print(f"[TCP] Connection lost: {e}")

    finally:
        conn.close()
        print("[TCP] Laptop disconnected.")


# ------------------------------------------------------------------ #
# Entry point
# ------------------------------------------------------------------ #
def main():
    arduino = ArduinoWriter()

    ard_thread = threading.Thread(target=arduino.run, daemon=True)
    ard_thread.start()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((LISTEN_HOST, LISTEN_PORT))
    srv.listen(1)

    print(f"[TCP] Listening on {LISTEN_HOST}:{LISTEN_PORT}")

    try:
        while True:
            conn, addr = srv.accept()
            t = threading.Thread(
                target=handle_client,
                args=(conn, addr, arduino),
                daemon=True,
            )
            t.start()

    except KeyboardInterrupt:
        print("\n[MAIN] Shutting down.")

    finally:
        arduino.stop()
        srv.close()


# if __name__ == "__main__":
#     main()