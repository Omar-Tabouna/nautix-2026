import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Front.login_front import Ui_LoginWindow
from pilot_back import PilotWindow
from copilot_back import CoPilotWindow


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        
        self.ui.login_btn.clicked.connect(self.choose_user)
        
    def choose_user(self):
        if self.ui.userbox.currentText() == "Pilot":
            self.pilotwindow = PilotWindow()
            self.pilotwindow.show()
        else:
            self.copilotwindow = CoPilotWindow()
            self.copilotwindow.show()
        self.close()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())