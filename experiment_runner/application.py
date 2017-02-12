from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox)
from PyQt5.QtCore import QTimer
from widgets import ModeSelector, UserDataInput


class Application(object):
    app = None
    controller = None
    args = None
    mode_select_widget = None
    user_info_widget = None

    _startup_timer = None

    def __init__(self, controller, args):
        self.controller = controller
        self.args = args

    def run(self):
        self.app = QApplication(self.args)
        self._startup_timer = QTimer().singleShot(0, self.on_started)
        return self.app.exec_()

    def on_started(self):
        if self.controller.has_data():
            self.show_purge_data_question()
        else:
            self.show_mode_select()

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
            self.controller.purge_data()
            self.show_mode_select()
        else:
            self.app_close()

    def show_mode_select(self):
        self.mode_select_widget = ModeSelector()
        self.mode_select_widget.show()
        self.mode_select_widget.finished.connect(self.on_mode_selected)
        self.mode_select_widget.rejected.connect(self.app_close)

    def on_mode_selected(self, selected_mode):
        print("Result: {}".format(selected_mode))
        self.controller.experiment_mode(selected_mode)
        self.ask_user_info()

    def ask_user_info(self):
        self.user_info_widget = UserDataInput(self.controller)
        self.user_info_widget.show()
        self.user_info_widget.accepted.connect(self.experiment_start)
        self.user_info_widget.rejected.connect(self.app_close)

    def experiment_start(self):
        pass

    def app_close(self):
        self.app.quit()
