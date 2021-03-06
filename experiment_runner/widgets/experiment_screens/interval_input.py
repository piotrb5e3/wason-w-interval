from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import QTimer, Qt
from dialog import UnrejectableDialog

no_clicking_color = QColor(252, 55, 65)
non_random_clicking_color = QColor(105, 244, 93)

S_TO_MS = 1000


class IntervalInput(UnrejectableDialog):
    click_controller = None
    timer = None
    orig_bg_color = None

    def __init__(self, click_controller):
        super().__init__()
        self.click_controller = click_controller
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_if_should_warn)
        self.timer.start(200)
        self.orig_bg_color = self.palette().color(QPalette.Window)

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self.click_controller.on_click()
            event.accept()

    def check_if_should_warn(self):
        if self.click_controller.is_not_clicking():
            self.warn_no_clicking()
        elif self.click_controller.is_clicking_rhythmically():
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
        p = self.palette()
        p.setColor(QPalette.Window, self.orig_bg_color)
        self.setPalette(p)
        self.setAutoFillBackground(True)


class TimedIntervalInput(IntervalInput):
    timeout_timer = None

    def __init__(self, click_controller, time_in_s):
        super().__init__(click_controller)
        self.timeout_timer = QTimer.singleShot(time_in_s * S_TO_MS, self.accept)
        click_controller.start()
