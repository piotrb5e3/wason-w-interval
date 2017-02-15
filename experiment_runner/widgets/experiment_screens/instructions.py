from PyQt5.QtWidgets import (QLabel, QPushButton,
                             QHBoxLayout, QDialog, QFrame, QGridLayout
                             )


class Instructions(QDialog):
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
        self.next = QPushButton("Continue")
        self.next.clicked.connect(self.accept)

        self.textBox = QLabel(self.text)

        grid = QGridLayout()
        grid.addWidget(self.textBox, 0, 0, 4, 0)
        grid.addWidget(self.next, 4, 1)

        frame.setLayout(grid)

        box = QHBoxLayout()
        box.addWidget(frame)
        box.setContentsMargins(300, 100, 300, 100)
        self.setLayout(box)
