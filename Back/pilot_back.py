import cv2
import threading

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, QObject, Signal
from PySide6.QtWidgets import QMainWindow

from Front.pilot_front import Ui_Pilot_Window
from joystick_thread import JoystickThread
from control.main import control_main
import time

PORTS = [5006, 5600, 5602]

class PilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pilot_Window()
        self.ui.setupUi(self)

        self.boxes = [self.ui.box1, self.ui.box2, self.ui.box3]
        self.labels = [self.ui.Cam1, self.ui.Cam2, self.ui.Cam3]
        self.threads = [VideoThread(port) for port in PORTS]

        for i, t in enumerate(self.threads):
            t.camera_image.connect(lambda img, i=i: self.update_label(i, img))
            t.start()

        self.display_map = [0, 1, 2]

        for i, box in enumerate(self.boxes):
            box.currentIndexChanged.connect(lambda _, i=i: self.change_camera(i))

        #############################################
        # TEST UI VALUES
        self.ui.Speed_bar.setValue(60)
        self.ui.Gain_bar.setValue(25)
        #############################################

        # 🔥 Joystick
        self.joystick_thread = JoystickThread(self)
        self.joystick_thread.moved.connect(self.on_joystick_moved)
        self.joystick_thread.start()

        # # 🔥 (Optional) Controller thread
        # self.controller_thread = threading.Thread(target=control_main, daemon=True)
        # self.controller_thread.start()

        self.control_system = control_main()
        self.control_system.start()

    def update_label(self, cam_index, qimg):
        for i, displayed_cam in enumerate(self.display_map):
            if displayed_cam == cam_index:

                pix = QPixmap.fromImage(qimg.copy())

                self.labels[i].setPixmap(
                    pix.scaled(self.labels[i].size(), Qt.KeepAspectRatio)
                )

    def on_throttle_up(self, is_up: bool):
        if is_up:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        else:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/red.png"))

    def on_joystick_moved(self, x: float, y: float):
        self.ui.joystick_animation.set_position(x, y)
        y = -y

        if y > 0:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        elif y < 0:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/red.png"))
        else:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))

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

    def closeEvent(self, event):
        for t in self.threads:
            t.stop()
        self.joystick_thread.stop()
        self.control_system.stop()
        event.accept()


class VideoThread(QThread):
    camera_image = Signal(QImage)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.cap = None
        self.running = True

    def build_pipeline(self, port):
        return (
            f'udpsrc port={port} caps="application/x-rtp,media=video,encoding-name=H264,payload=96" ! '
            'rtpjitterbuffer latency=0 ! '
            'rtph264depay ! avdec_h264 ! '
            'videoconvert ! appsink drop=true max-buffers=1'
        )

    def run(self):
        print(f"[CAM {self.port}] THREAD STARTED")

        pipeline = self.build_pipeline(self.port)

        while self.running:
            try:
                time.sleep(0.5)

                self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

                if not self.cap.isOpened():
                    print(f"[CAM {self.port}] FAILED TO OPEN")
                    self.msleep(500)
                    continue

                print(f"[CAM {self.port}] STREAM OPENED")

                while self.running:
                    ret, frame = self.cap.read()

                    if not ret or frame is None:
                        print(f"[CAM {self.port}] bad frame")
                        continue

                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb.shape

                    qimg = QImage(w, h, QImage.Format_RGB888)
                    qimg.bits()[:] = rgb.tobytes()

                    self.camera_image.emit(qimg)

                    self.msleep(50)

            except Exception as e:
                print(f"[CAM {self.port}] ERROR:", e)

            if self.cap:
                self.cap.release()

            self.msleep(500)

    def stop(self):
        self.running = False
        if self.cap:
            self.cap.release()
        self.wait()