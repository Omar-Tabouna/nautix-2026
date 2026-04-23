import cv2

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, Signal
from PySide6.QtWidgets import QMainWindow

from Front.pilot_front import Ui_Pilot_Window
from control.main import control_main
from Back.zmqthread import ZMQThread
import time

PORTS = [5006, 5600, 5602]


class PilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pilot_Window()
        self.ui.setupUi(self)

        self.boxes = [self.ui.box1, self.ui.box2, self.ui.box3]
        self.labels = [self.ui.Cam2, self.ui.Cam3]

        # display_map[slot] = which UDP camera index (1–3) is shown in labels[slot]
        self.display_map = [1, 2, 3]

        # UDP cameras (indices 1–3)
        self.threads = [VideoThread(port) for port in PORTS]
        for i, t in enumerate(self.threads):
            cam_index = i + 1
            t.camera_image.connect(
                lambda img, ci=cam_index: self.route_frame(ci, img)
            )
            t.start()

        # ZMQ / OAK camera — shown on self.ui.Camera (its own dedicated label)
        self.zmq_thread = ZMQThread(address="192.168.33.1", port="5454")
        self.zmq_thread.frame_ready.connect(self.update_oak_label)
        self.zmq_thread.disconnected.connect(self.on_cam_disconnected)
        self.zmq_thread.start()

        for i, box in enumerate(self.boxes):
            box.currentIndexChanged.connect(lambda _, i=i: self.change_camera(i))

        #############################################
        # TEST UI VALUES
        self.ui.Speed_bar.setValue(60)
        self.ui.Gain_bar.setValue(25)
        #############################################

        self.control_system = control_main()
        self.control_system.new_data.connect(self.update_ui)
        self.control_system.start()

    # ------------------------------------------------------------------
    # Camera routing
    # ------------------------------------------------------------------

    def route_frame(self, cam_index, img):
        """Route a UDP camera frame to whichever slot it is mapped to."""
        pix = QPixmap.fromImage(img)
        for slot, mapped_cam in enumerate(self.display_map):
            if mapped_cam == cam_index:
                label = self.labels[slot]
                label.setPixmap(pix.scaled(label.size(), Qt.KeepAspectRatio))
                return

    def update_oak_label(self, img):
        """Display the OAK/ZMQ frame on its dedicated label."""
        pix = QPixmap.fromImage(img)
        label = self.ui.Cam1
        label.setPixmap(pix.scaled(label.size(), Qt.KeepAspectRatio))

    def change_camera(self, changed_slot):
        """Swap camera assignments when a combo-box selection changes."""
        new_cam = self.boxes[changed_slot].currentIndex() + 1
        old_cam = self.display_map[changed_slot]

        if new_cam == old_cam:
            return

        for i in range(len(self.display_map)):
            if i != changed_slot and self.display_map[i] == new_cam:
                self.boxes[i].blockSignals(True)
                self.boxes[i].setCurrentIndex(old_cam - 1)
                self.boxes[i].blockSignals(False)
                self.display_map[i] = old_cam
                break

        self.display_map[changed_slot] = new_cam

    # ------------------------------------------------------------------
    # UI updates from control system
    # ------------------------------------------------------------------

    def on_cam_disconnected(self):
        print("[ZMQ] Stream lost")

    def update_ui(self, msg: dict):
        if msg.get("camera") is not None:
            new_cam = msg["camera"] + 1          # controller index 0-based → cam 1-based
            old_cam = self.display_map[0]

            if new_cam != old_cam:
                # if new_cam is already shown in another slot, swap
                for i in range(1, len(self.display_map)):
                    if self.display_map[i] == new_cam:
                        self.display_map[i] = old_cam
                        self.boxes[i].blockSignals(True)
                        self.boxes[i].setCurrentIndex(old_cam - 1)
                        self.boxes[i].blockSignals(False)
                        break

                self.display_map[0] = new_cam
                self.boxes[0].blockSignals(True)
                self.boxes[0].setCurrentIndex(new_cam - 1)
                self.boxes[0].blockSignals(False)
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

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------

    def closeEvent(self, event):
        for t in self.threads:
            t.stop()
        self.zmq_thread.stop()
        self.control_system.stop()
        event.accept()


# ----------------------------------------------------------------------

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
                    qimg = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)
                    self.camera_image.emit(qimg.copy())
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