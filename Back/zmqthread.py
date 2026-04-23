import zmq
import cv2
import numpy as np

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage


class ZMQThread(QThread):
    frame_ready = Signal(QImage)
    disconnected = Signal()

    def __init__(self, address="192.168.33.1", port="5454"):
        super().__init__()
        self.address = address
        self.port = port
        self.running = True

    def run(self):
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://{self.address}:{self.port}")
        socket.setsockopt(zmq.SUBSCRIBE, b"")
        socket.setsockopt(zmq.RCVTIMEO, 2000)  # 2s timeout so stop() isn't blocked

        print(f"[ZMQ] Connected to tcp://{self.address}:{self.port}")

        while self.running:
            try:
                buffer = socket.recv()
            except zmq.Again:
                # Timeout — no frame received, loop back and check self.running
                self.disconnected.emit()
                continue
            except zmq.ZMQError as e:
                print(f"[ZMQ] Error: {e}")
                break

            arr = np.frombuffer(buffer, dtype=np.uint8)
            frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)
            if frame is None:
                continue

            frame = cv2.rotate(frame, cv2.ROTATE_180)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
            self.frame_ready.emit(qimg.copy())

        socket.close()
        context.term()
        print("[ZMQ] Thread stopped")

    def stop(self):
        self.running = False
        self.wait()