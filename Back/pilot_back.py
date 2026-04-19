import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, QTimer
from PySide6.QtWidgets import QMainWindow

from Front.pilot_front import Ui_Pilot_Window

RTSP_URLS = [
    "rtsp://192.168.33.1:8554/cam1",
    "rtsp://192.168.33.1:8554/cam2",
    "rtsp://192.168.33.1:8554/cam3",
    "rtsp://192.168.33.1:8554/cam4",
]

class PilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pilot_Window()
        self.ui.setupUi(self)

        self.boxes = [self.ui.box1, self.ui.box2, self.ui.box3]
        self.labels = [self.ui.Cam1, self.ui.Cam2, self.ui.Cam3]

        self.threads = [VideoThread(url) for url in RTSP_URLS]
        for t in self.threads:
            t.start()
            
        self.display_map = [0, 1, 2]

        for i, box in enumerate(self.boxes):
            box.currentIndexChanged.connect(lambda _, i=i: self.change_camera(i))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frames)
        self.timer.start(30)
        
        #############################################
        # TEST UI VALUES
        self.ui.Speed_bar.setValue(60)
        self.ui.Gain_bar.setValue(25)
        #############################################

    def change_camera(self, changed_index):
        new_cam = self.boxes[changed_index].currentIndex()
        old_cam = self.display_map[changed_index]

        for i in range(len(self.display_map)):
            if i != changed_index and self.display_map[i] == new_cam:
                self.boxes[i].blockSignals(True)
                self.boxes[i].setCurrentIndex(old_cam)
                self.boxes[i].blockSignals(False)
                self.display_map[i] = old_cam
                break

        self.display_map[changed_index] = new_cam

    def update_frames(self):
        for i, cam_index in enumerate(self.display_map):
            thread = self.threads[cam_index]

            if thread.frame is None:
                self.labels[i].setText("NO SIGNAL")
                continue

            frame = thread.frame
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape

            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            pix = QPixmap.fromImage(qimg)

            self.labels[i].setPixmap(
                pix.scaled(self.labels[i].size(), Qt.KeepAspectRatio)
            )

    def closeEvent(self, event):
        for t in self.threads:
            t.stop()
        event.accept()
        

class VideoThread(QThread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.cap = None
        self.frame = None
        self.running = True

    def build_pipeline(self, url):
        return (
            f"rtspsrc location={url} latency=0 protocols=udp ! "
            "rtph264depay ! decodebin ! videoconvert ! appsink drop=1"
        )

    def run(self):
        while self.running:
            try:
                pipeline = self.build_pipeline(self.url)
                self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

                if not self.cap.isOpened():
                    print(f"[ERROR] Cannot open {self.url}")
                    self.msleep(1000)
                    continue

                while self.running:
                    ret, frame = self.cap.read()
                    if not ret:
                        break
                    self.frame = frame

            except Exception as e:
                print(e)

            if self.cap:
                self.cap.release()

            self.msleep(500)

    def stop(self):
        self.running = False
        self.wait()
