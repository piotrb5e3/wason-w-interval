from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QMargins
from PyQt5.QtGui import QFont, QPainter, QColor


class WrappingTextField(QWidget):
    font_family = None
    font_size = None
    font_color = None
    text = None

    def __init__(self, text, font_family='Serif', font_size=10,
                 font_color=QColor(0, 0, 0)):
        super().__init__()
        self.font_family = font_family
        self.font_size = font_size
        self.font_color = font_color
        self.text = text

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter()
        qp.begin(self)
        self.draw_text(event, qp)
        qp.end()

    def draw_text(self, event, qp):
        draw_rect = event.rect().marginsRemoved(QMargins(5, 5, 5, 5))
        qp.setPen(self.font_color)
        qp.setFont(QFont(self.font_family, self.font_size))
        qp.drawText(draw_rect, Qt.TextWordWrap | Qt.AlignLeft, self.text)
