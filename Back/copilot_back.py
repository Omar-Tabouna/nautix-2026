import cv2
import time

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, Signal, QTimer
from PySide6.QtWidgets import QMainWindow

from Front.copilot_front import Ui_CoPilot_Window
from joystick_thread import JoystickThread

PORTS = [5006, 5600, 5602, 5604]


class CoPilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CoPilot_Window()
        self.ui.setupUi(self)

        # ---------------- CAMERA THREAD ----------------
        self.thread = VideoThread(PORTS[0])
        self.thread.camera_image.connect(self.update_frame)
        self.thread.start()

        # ---------------- CAMERA SWITCH ----------------
        self.ui.cambtn1.clicked.connect(lambda: self.change_camera(PORTS[0]))
        self.ui.cambtn2.clicked.connect(lambda: self.change_camera(PORTS[1]))
        self.ui.cambtn3.clicked.connect(lambda: self.change_camera(PORTS[2]))
        self.ui.cambtn4.clicked.connect(lambda: self.change_camera(PORTS[3]))

        # ---------------- CLOCK ----------------
        self.ui.lcdNumber.display("15:00")
        self.seconds = 15 * 60

        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)

        self.ui.start_btn.clicked.connect(self.start_clock)
        self.ui.reset_btn.clicked.connect(self.reset_clock)
        self.ui.pausebtn.clicked.connect(self.pause_clock)

        # ---------------- TEST UI ----------------
        self.ui.Speed_bar.setValue(60)
        self.ui.Gain_bar.setValue(25)
        self.ui.Stabilizer_label.setStyleSheet("background-color: rgb(0, 255, 0);")

        # ---------------- JOYSTICK ----------------
        self.joystick_thread = JoystickThread(self)
        self.joystick_thread.moved.connect(self.on_joystick_moved)
        self.joystick_thread.start()

    # ================= CAMERA =================
    def update_frame(self, qimg):
        pix = QPixmap.fromImage(qimg.copy())
        self.ui.Camera.setPixmap(
            pix.scaled(self.ui.Camera.size(), Qt.KeepAspectRatio)
        )

    def change_camera(self, port):
        self.thread.change_camera(port)

    # ================= JOYSTICK =================
    def on_joystick_moved(self, x: float, y: float):
        self.ui.joystick_animation.set_position(x, y)

    # ================= CLOCK =================
    def update_clock(self):
        if self.seconds >= 0:
            self.seconds -= 1
            self.ui.lcdNumber.display(
                f"{self.seconds // 60:02d}:{self.seconds % 60:02d}"
            )

    def start_clock(self):
        self.clock_timer.start(1000)

    def reset_clock(self):
        self.seconds = 15 * 60
        self.ui.lcdNumber.display("15:00")
        self.clock_timer.stop()

    def pause_clock(self):
        self.clock_timer.stop()

    # ================= CLEANUP =================
    def closeEvent(self, event):
        self.thread.stop()
        self.joystick_thread.stop()
        event.accept()


# ================= VIDEO THREAD =================
class VideoThread(QThread):
    camera_image = Signal(QImage)

    def __init__(self, port):
        super().__init__()
        self.port = port
        self.running = True

    def build_pipeline(self, port):
        return (
            f'udpsrc port={port} caps="application/x-rtp,media=video,encoding-name=H264,payload=96" ! '
            'rtpjitterbuffer latency=0 ! '
            'rtph264depay ! avdec_h264 ! '
            'videoconvert ! appsink drop=true max-buffers=1'
        )

    def run(self):
        print(f"[CAM {self.port}] STARTED")

        while self.running:
            pipeline = self.build_pipeline(self.port)
            cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

            if not cap.isOpened():
                print(f"[CAM {self.port}] FAILED")
                self.msleep(500)
                continue

            print(f"[CAM {self.port}] STREAM OPENED")

            while self.running:
                ret, frame = cap.read()

                if not ret or frame is None:
                    continue

                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape

                qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888).copy()

                self.camera_image.emit(qimg)
                self.msleep(50)

            cap.release()

    def change_camera(self, port):
        self.port = port

    def stop(self):
        self.running = False
        self.wait()