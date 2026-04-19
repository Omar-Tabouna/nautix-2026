import pygame
from PySide6.QtCore import QThread, Signal

class JoystickThread(QThread):
    moved = Signal(float, float)   # (x, y) in [-1.0, 1.0]

    DEAD_ZONE = 0.05   # ignore tiny axis drift near center
    POLL_MS   = 16     # ~60 Hz

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = True

    def run(self):
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            print("[JoystickThread] No joystick detected.")
            return

        joy = pygame.joystick.Joystick(0)
        joy.init()
        print(f"[JoystickThread] Connected: {joy.get_name()}")

        while self._running:
            pygame.event.pump()

            x = joy.get_axis(0)   # left stick horizontal
            y = joy.get_axis(1)   # left stick vertical

            # apply dead zone
            if abs(x) < self.DEAD_ZONE:
                x = 0.0
            if abs(y) < self.DEAD_ZONE:
                y = 0.0

            self.moved.emit(round(x, 3), round(y, 3))
            self.msleep(self.POLL_MS)

        pygame.quit()

    def stop(self):
        self._running = False
        self.wait()   # block until thread finishes