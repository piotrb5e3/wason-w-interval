from PyQt5.QtWidgets import (QLabel, QPushButton,
                             QHBoxLayout, QDialog, QWidget, QGridLayout
                             )
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QTimer

no_clicking_color = QColor(252, 55, 65)
non_random_clicking_color = QColor(105, 244, 93)


class IntervalInput(QDialog):
    controller = None
    timer = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_if_should_warn)
        self.timer.start(200)

    def init_ui(self):
        self.setGeometry(100, 100, 300, 300)

    def check_if_should_warn(self):
        if self.controller.is_not_clicking():
            self.warn_no_clicking()
        elif self.controller.is_clicking_rhytmicly():
            self.warn_non_random_intervals()
        else:
            self.set_no_warning()

    def warn_no_clicking(self):
        p = self.palette()
        p.setColor(QPalette.Window, no_clicking_color)
        self.setPalette(p)
        self.setAutoFillBackground(True)

    def warn_non_random_intervals(self):
        p = self.palette()
        p.setColor(QPalette.Window, non_random_clicking_color)
        self.setPalette(p)
        self.setAutoFillBackground(True)

    def set_no_warning(self):
        self.setAutoFillBackground(False)


class TimedIntervalInput(IntervalInput):
    timeout_timer = None

    def __init__(self, controller, time):
        super().__init__(controller)
        self.timeout_timer = QTimer.singleShot(time, self.accept)
