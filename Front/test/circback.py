import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
from circfront import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.updatetime)
        # self.timer.start(10)
        self.ui.progress.setValue(65)
        
    def updatetime(self):
        if self.ui.progress.value < 100:
            self.ui.progress.setValue(self.ui.progress.value)
            self.ui.progress.value += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


