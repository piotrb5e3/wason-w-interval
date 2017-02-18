from PyQt5.QtWidgets import QWidget


class CardSelectionsConfigTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
