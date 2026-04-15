from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QColor, QFont
from PySide6.QtCore import Qt, QRectF

class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.update()  # trigger repaint

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        margin = 10

        rect = QRectF(margin, margin, width - 2*margin, height - 2*margin)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 🔘 Background circle
        pen = QPen(QColor("#e6e6e6"), 10)
        painter.setPen(pen)
        painter.drawEllipse(rect)

        # 🔵 Progress arc
        pen.setColor(QColor("#3498db"))
        painter.setPen(pen)

        
        # angle: start at top (90°), go clockwise negative
        span_angle = int(-360 * self.value / 100)
        painter.drawArc(rect, 90 * 16, span_angle * 16)

        # 🔢 Text
        painter.setPen(Qt.white)
        painter.setFont(QFont("Arial", 14, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, f"{self.value}%")