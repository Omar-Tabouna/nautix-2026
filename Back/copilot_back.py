import cv2

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, Signal, QTimer
from PySide6.QtWidgets import QMainWindow

from Front.copilot_front import Ui_CoPilot_Window
from control.main import control_main
from Back.zmqthread import ZMQThread

# UDP ports for cams 1–3 (cam 0 is OAK via ZMQ)
PORTS = [5600, 5602, 5604]


class CoPilotWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_CoPilot_Window()
        self.ui.setupUi(self)

        # frames[0] = OAK/ZMQ, frames[1–3] = UDP cams
        self.frames = [None] * 4
        self.current_camera = 0

        # ---------------- ZMQ / OAK (cam 0) ----------------
        self.zmq_thread = ZMQThread(address="192.168.33.1", port="5454")
        self.zmq_thread.frame_ready.connect(lambda img: self.store_frame(img, 0))
        self.zmq_thread.disconnected.connect(lambda: print("[ZMQ] Stream lost"))
        self.zmq_thread.start()

        # ---------------- UDP CAMERAS (cams 1–3) ----------------
        self.threads = []
        for i, port in enumerate(PORTS):
            thread = VideoThread(port, i + 1)
            thread.camera_image.connect(self.store_frame)
            thread.start()
            self.threads.append(thread)

        # ---------------- CAMERA SWITCH ----------------
        self.ui.cambtn1.clicked.connect(lambda: self.switch_camera(0))
        self.ui.cambtn2.clicked.connect(lambda: self.switch_camera(1))
        self.ui.cambtn3.clicked.connect(lambda: self.switch_camera(2))
        self.ui.cambtn4.clicked.connect(lambda: self.switch_camera(3))

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

        self.control_system = control_main()
        self.control_system.new_data.connect(self.update_ui)
        self.control_system.start()

    # ================= CAMERA =================

    def store_frame(self, qimg, index):
        self.frames[index] = qimg
        if index == self.current_camera:
            self.update_frame(qimg)

    def update_frame(self, qimg):
        pix = QPixmap.fromImage(qimg.copy())
        self.ui.Camera.setPixmap(
            pix.scaled(self.ui.Camera.size(), Qt.KeepAspectRatio)
        )

    def switch_camera(self, index):
        self.current_camera = index
        if self.frames[index] is not None:
            self.update_frame(self.frames[index])

    # ================= UI =================

    def update_ui(self, msg: dict):
        lx = msg["left_x"]
        ly = msg["left_y"]
        rx = msg["right_x"]

        self.ui.Gain_bar.setValue(msg["gain"])

        if msg["gripper_a"]:
            self.ui.Hgripper_label.setPixmap(QPixmap(u":/Front/icons/closed_Hgripper.png"))
        else:
            self.ui.Hgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Hgripper.png"))

        if msg["gripper_b"]:
            self.ui.Vgripper_label.setPixmap(QPixmap(u":/Front/icons/closed_Vgripper.png"))
        else:
            self.ui.Vgripper_label.setPixmap(QPixmap(u":/Front/icons/open_Vgripper.png"))

        if rx > 0:
            self.ui.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow1.png"))
            self.ui.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow2.png"))
        elif rx < 0:
            self.ui.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow2.png"))
            self.ui.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow1.png"))
        else:
            self.ui.cw_label.setPixmap(QPixmap(u":/Front/icons/cw_arrow2.png"))
            self.ui.acw_label.setPixmap(QPixmap(u":/Front/icons/acw_arrow2.png"))

        if ly < 0:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))
        elif ly > 0:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/red.png"))
        else:
            self.ui.thrustup_label.setPixmap(QPixmap(u":/Front/icons/light_green.png"))
            self.ui.thrustdown_label.setPixmap(QPixmap(u":/Front/icons/light_red.png"))

        self.ui.joystick_animation.set_position(lx, ly)

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
        self.zmq_thread.stop()
        for thread in self.threads:
            thread.stop()
        self.control_system.stop()
        event.accept()


# ================= VIDEO THREAD =================

class VideoThread(QThread):
    camera_image = Signal(QImage, int)

    def __init__(self, port, index):
        super().__init__()
        self.port = port
        self.index = index
        self.running = True

    def build_pipeline(self, port):
        return (
            f'udpsrc port={port} caps="application/x-rtp,media=video,encoding-name=H264,payload=96" ! '
            'rtpjitterbuffer latency=0 ! '
            'rtph264depay ! avdec_h264 ! '
            'videoconvert ! appsink drop=true max-buffers=1'
        )

    def run(self):
        print(f"[CAM {self.index}] STARTED (Port {self.port})")
        pipeline = self.build_pipeline(self.port)
        cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

        if not cap.isOpened():
            print(f"[CAM {self.index}] FAILED TO OPEN")
            return

        print(f"[CAM {self.index}] STREAM OPENED")

        while self.running:
            ret, frame = cap.read()
            if not ret or frame is None:
                continue

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888).copy()
            self.camera_image.emit(qimg, self.index)
            self.msleep(5)

        cap.release()
        print(f"[CAM {self.index}] STOPPED")

    def stop(self):
        self.running = False
        self.wait()