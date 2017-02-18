from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QMessageBox)

from controller import ConfigController
from widgets import NewOrLoad


class Application(object):
    new_or_load = None
    app = None
    args = None
    mode_select_widget = None
    user_info_widget = None
    experiment_window = None
    controller = None

    _startup_timer = None

    def __init__(self, args):
        self.args = args
        self.controller = ConfigController()

    def run(self):
        self.app = QApplication(self.args)
        self._startup_timer = QTimer().singleShot(0, self.on_started)
        return self.app.exec_()

    def on_started(self):
        self.ask_new_or_load()

    def ask_new_or_load(self):
        self.new_or_load = NewOrLoad(self.controller)
        self.new_or_load.accepted.connect(self.open_configurator)

    def open_configurator(self):
        pass
