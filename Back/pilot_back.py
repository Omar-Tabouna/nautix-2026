import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, QTimer

from PySide6.QtWidgets import QMainWindow
from Front.pilot_front import Ui_Pilot_Window


class PilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pilot_Window()
        self.ui.setupUi(self)

        self.boxes = [self.ui.box1, self.ui.box2, self.ui.box3, self.ui.box4]
        self.threads = [VideoThread(box.currentIndex()) for box in self.boxes]
        self.labels = [self.ui.Cam1, self.ui.Cam2, self.ui.Cam3, self.ui.Cam4]


        for i, box in enumerate(self.boxes):
            box.currentTextChanged.connect(lambda _, i=i: self.change_camera(i))

        for t in self.threads:
            t.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frames)
        self.timer.start(15)
        
        ############################################# for testing ###################################################
        self.ui.Speed_bar.setValue(60)
        self.ui.Gain_bar.setValue(25)
        #############################################################################################################

    def change_camera(self, changed_index):
        new_cam = self.boxes[changed_index].currentIndex()
        old_cam = self.threads[changed_index].cam_index 

        conflict_index = None
        for i, box in enumerate(self.boxes):
            if i != changed_index and box.currentIndex() == new_cam:
                conflict_index = i
                break

        self.threads[changed_index].cam_index = new_cam
        self.threads[changed_index].new_cam_index = new_cam

        if conflict_index is not None:
            self.boxes[conflict_index].blockSignals(True)
            self.boxes[conflict_index].setCurrentIndex(old_cam)
            self.boxes[conflict_index].blockSignals(False)
            self.threads[conflict_index].cam_index = old_cam
            self.threads[conflict_index].new_cam_index = old_cam

    def update_frames(self):
        for i, t in enumerate(self.threads):
            if t.frame is None:
                continue

            rgb = cv2.cvtColor(t.frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            pix = QPixmap.fromImage(qimg)
            self.labels[i].setPixmap(
                pix.scaled(self.labels[i].size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        
    def closeEvent(self, event):
        for t in self.threads:
            t.stop()
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
        self.cam_index = cam_index
        self.new_cam_index = cam_index 

    def run(self):
        self.cap = cv2.VideoCapture(self.cam_index)

        while self.running:
            if self.new_cam_index is not None:
                self.cap.release()
                self.cam_index = self.new_cam_index
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