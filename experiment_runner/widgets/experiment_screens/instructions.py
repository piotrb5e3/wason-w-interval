from PyQt5.QtWidgets import (QLabel, QPushButton,
                             QHBoxLayout, QDialog, QWidget, QGridLayout
                             )


class Instructions(QDialog):
    text = None
    textBox = None
    next = None

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        self.next = QPushButton("Continue")
        self.next.clicked.connect(self.accept)

        self.textBox = QLabel(self.text)

        grid = QGridLayout()
        grid.addWidget(self.textBox, 0, 0, 4, 4)
        grid.addWidget(self.next, 4, 5)

        self.setLayout(grid)
