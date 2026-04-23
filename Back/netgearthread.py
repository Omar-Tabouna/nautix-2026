from vidgear.gears import NetGear
import cv2
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

class NetGearThread(QThread):
    frame_ready = Signal(QImage)
    disconnected = Signal()

    def __init__(self, address="192.168.33.2", port="5454"):
        super().__init__()
        self.address = address
        self.port = port
        self._running = True

    def run(self):
        client = NetGear(
            receive_mode=True,
            address=self.address,
            port=self.port,
            protocol="tcp",
            pattern=1,
            logging=True
        )

        while self._running:
            frame = client.recv()
            if frame is None:
                self.disconnected.emit()
                break

            frame = cv2.rotate(frame, cv2.ROTATE_180)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
            self.frame_ready.emit(qimg.copy())

        client.close()

    def stop(self):
        self._running = False
        self.quit()
        self.wait()