import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, QTimer

from PySide6.QtWidgets import QMainWindow
from Front.copilot_front import Ui_CoPilot_Window


class CoPilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CoPilot_Window()
        self.ui.setupUi(self)
        
        self.thread = VideoThread(self.ui.comboBox_4.currentIndex())
        self.thread.start()
        self.ui.comboBox_4.currentTextChanged.connect(self.change_camera)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frames)
        self.timer.start(30)

    
    def change_camera(self):
        cam_index = self.ui.comboBox_4.currentIndex()
        self.thread.change_camera(cam_index)


    def update_frames(self):
        if self.thread.frame is None:
            return

        frame = self.thread.frame
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)
        self.ui.Camera.setPixmap(
            pix.scaled(
                self.ui.Camera.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        
    def closeEvent(self, event):
        self.thread.stop()
        event.accept()



class VideoThread(QThread):
    def __init__(self, cam_index):
        super().__init__()
        self.cam_index = cam_index
        self.cap = None
        self.running = True
        self.frame = None
        self.new_cam_index = None
        
        
    def change_camera(self, cam_index):
        self.new_cam_index = cam_index 

    def run(self):
        self.cap = cv2.VideoCapture(self.cam_index)

        while self.running:
            if self.new_cam_index is not None:
                self.cap.release()
                self.cap = cv2.VideoCapture(self.new_cam_index)
                self.new_cam_index = None

            ret, frame = self.cap.read()

            if not ret:
                continue

            self.frame = frame

            fps = self.cap.get(cv2.CAP_PROP_FPS)
            delay = int(1000 / fps) if fps > 0 else 33

            self.msleep(delay)

        self.cap.release()

    def stop(self):
        self.running = False
        self.wait()