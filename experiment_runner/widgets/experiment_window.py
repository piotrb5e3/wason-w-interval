from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMainWindow)


class ExperimentWindow(QMainWindow):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        pass
