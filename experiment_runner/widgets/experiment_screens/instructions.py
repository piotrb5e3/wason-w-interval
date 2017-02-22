from PyQt5.QtWidgets import (QPushButton, QVBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from dialog import UnrejectableDialog
from .text_field import WrappingTextField


class Instructions(UnrejectableDialog):
    text = None
    textBox = None
    next = None

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)
        frame.setFixedSize(1200, 700)

        self.next = QPushButton("Continue")
        self.next.clicked.connect(self.accept)

        self.textBox = WrappingTextField(text=self.text, font_size=11)

        vbox = QVBoxLayout()
        vbox.addWidget(self.textBox)
        vbox.addWidget(self.next, alignment=Qt.AlignRight)

        frame.setLayout(vbox)

        box = QVBoxLayout()
        box.addWidget(frame, alignment=Qt.AlignCenter)
        self.setLayout(box)
