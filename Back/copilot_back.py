import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Qt, QTimer
from PySide6.QtWidgets import QMainWindow

from Front.copilot_front import Ui_CoPilot_Window
from joystick_thread import JoystickThread

RTSP_URLS = [
    "rtsp://192.168.33.1:8554/cam1",
    "rtsp://192.168.33.1:8554/cam2",
    "rtsp://192.168.33.1:8554/cam3",
    "rtsp://192.168.33.1:8554/cam4",
]


class CoPilotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CoPilot_Window()
        self.ui.setupUi(self)

        self.thread = VideoThread(0)
        self.thread.start()

        self.ui.cambtn1.clicked.connect(lambda: self.change_camera(0))
        self.ui.cambtn2.clicked.connect(lambda: self.change_camera(1))
        self.ui.cambtn3.clicked.connect(lambda: self.change_camera(2))
        self.ui.cambtn4.clicked.connect(lambda: self.change_camera(3))

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frames)
        self.timer.start(15)
        
        self.clock_timer = QTimer() 
        self.ui.lcdNumber.display("15:00") 
        self.seconds = 15*60 
        self.clock_timer.timeout.connect(self.update_clock) 
        self.ui.start_btn.clicked.connect(lambda: self.clock_timer.start(1000)) 
        self.ui.reset_btn.clicked.connect(self.reset_clock)
        self.ui.pausebtn.clicked.connect(self.pause_clock) 
        
        ############################################# for testing ################################################### 
        self.ui.Speed_bar.setValue(60) 
        self.ui.Gain_bar.setValue(25)
        
        self.ui.Stabilizer_label.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        #############################################################################################################
        
        self.joystick_thread = JoystickThread(self)
        self.joystick_thread.moved.connect(self.on_joystick_moved)
        self.joystick_thread.start()
    
    def on_joystick_moved(self, x: float, y: float):
        self.ui.joystick_animation.set_position(x, y)

    def update_clock(self): 
        if self.seconds >= 0: 
            self.seconds -= 1 
            self.ui.lcdNumber.display(f"{self.seconds//60:02d}:{self.seconds%60:02d}") 
            
    def reset_clock(self): 
        self.clock_timer.stop() 
        self.ui.lcdNumber.display("15:00")
        
    def pause_clock(self):
        self.clock_timer.stop()
        
        
    def change_camera(self, index):
        self.thread.change_camera(index)

    def update_frames(self):
        if self.thread.frame is None:
            self.ui.Camera.setText("NO SIGNAL")
            return

        frame = self.thread.frame
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape

        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg)

        self.ui.Camera.setPixmap(
            pix.scaled(self.ui.Camera.size(), Qt.KeepAspectRatio)
        )

    def closeEvent(self, event):
        self.thread.stop()
        self.joystick_thread.stop()
        event.accept()


class VideoThread(QThread):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.new_index = None
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
                url = RTSP_URLS[self.index]
                pipeline = self.build_pipeline(url)

                self.cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

                if not self.cap.isOpened():
                    print("[ERROR] Cannot open stream")
                    self.msleep(1000)
                    continue

                while self.running:
                    if self.new_index is not None:
                        self.cap.release()
                        self.index = self.new_index
                        self.new_index = None
                        break

                    ret, frame = self.cap.read()
                    if not ret:
                        break

                    self.frame = frame

            except Exception as e:
                print(e)

            if self.cap:
                self.cap.release()

            self.msleep(500)

    def change_camera(self, index):
        self.new_index = index

    def stop(self):
        self.running = False
        self.wait()
        