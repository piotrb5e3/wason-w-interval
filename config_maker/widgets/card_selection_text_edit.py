from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QVBoxLayout,
                             QPushButton, QHBoxLayout)


class CSTextEditTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
