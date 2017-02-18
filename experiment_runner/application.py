from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QMessageBox, QFileDialog)

from .widgets import ModeSelector, UserDataInput, ExperimentWindow

from config import load_config, ConfigException

from controllers import ExperimentController


class Application(object):
    app = None
    controller = None
    storage = None
    args = None
    mode_select_widget = None
    user_info_widget = None
    experiment_window = None

    _startup_timer = None

    def __init__(self, storage, args):
        self.args = args
        self.storage = storage

    def run(self):
        self.app = QApplication(self.args)
        self._startup_timer = QTimer().singleShot(0, self.on_started)
        return self.app.exec_()

    def on_started(self):
        if self.storage.has_data():
            self.show_purge_data_question()
        else:
            self.select_conf_file()

    def show_purge_data_question(self):
        reply = QMessageBox.question(None,
                                     'Warning',
                                     "There exists saved data from previous "
                                     "experiments. Continuing will result in "
                                     "deletion of this data. Do you want to "
                                     "continue?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No
                                     )
        if reply == QMessageBox.Yes:
            self.storage.purge()
            self.select_conf_file()
        else:
            self.app_close()

    def select_conf_file(self):
        fname = QFileDialog.getOpenFileName(
            None,
            'Open file',
            filter='Experiment Configuration (*.conf)')

        fname = fname[0]

        if not fname:
            self.app_close()
            return
        try:
            conf = load_config(fname)
        except ConfigException:
            self.app_close()
            return

        self.controller = ExperimentController(conf, self.storage)
        self.show_mode_select()

    def show_mode_select(self):
        self.mode_select_widget = ModeSelector(self.controller)
        self.mode_select_widget.finished.connect(self.ask_user_info)
        self.mode_select_widget.rejected.connect(self.app_close)
        self.mode_select_widget.show()

    def ask_user_info(self):
        self.user_info_widget = UserDataInput(self.controller)
        self.user_info_widget.accepted.connect(self.experiment_start)
        self.user_info_widget.rejected.connect(self.app_close)
        self.user_info_widget.show()

    def experiment_start(self):
        self.experiment_window = ExperimentWindow(self.controller)
        self.experiment_window.showFullScreen()

    def app_close(self):
        self.app.quit()
