from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QPoint, Signal
from PySide6.QtGui import QPainter, QColor, QPen, QBrush

class JoyStickWidget(QWidget):
    moved = Signal(float, float)  # emits (x, y) in [-1.0, 1.0]

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 200)
        self._thumb = QPoint(100, 100)

    def center(self):
        return QPoint(self.width() // 2, self.height() // 2)

    def radius(self):
        return min(self.width(), self.height()) // 2 - 2

    def set_position(self, x: float, y: float):
        """Called by the thread to move the thumb dot."""
        c, r = self.center(), self.radius()
        self._thumb = QPoint(
            int(c.x() + x * r),
            int(c.y() + y * r)
        )
        self.update()  # triggers paintEvent

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        cx = self.center().x()
        cy = self.center().y()
        r  = self.radius()

        # outer circle (background)
        p.setPen(QPen(QColor("#888888"), 2))
        p.setBrush(QBrush(QColor("#e0e0e0")))
        p.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        # center crosshair (optional guide)
        p.setPen(QPen(QColor("#bbbbbb"), 1))
        p.drawLine(cx - r, cy, cx + r, cy)
        p.drawLine(cx, cy - r, cx, cy + r)

        # thumb dot (inner circle)
        tr = r // 2
        tx = self._thumb.x()
        ty = self._thumb.y()
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor("#4670A0")))
        p.drawEllipse(tx - tr, ty - tr, tr * 2, tr * 2)

