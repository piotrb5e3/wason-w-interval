from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout)
from widgets import ModeSelector, UserDataInput


class Application(object):
    app = None
    controller = None
    args = None
    main_window = None
    mode_select_widget = None
    user_info_widget = None

    def __init__(self, controller, args):
        self.controller = controller
        self.args = args

    def run(self):
        self.app = QApplication(self.args)
        self.main_window = QWidget()
        self.main_window.show()
        self.mode_select_widget = ModeSelector()
        self.mode_select_widget.show()
        self.mode_select_widget.finished.connect(self.on_mode_selected)
        self.mode_select_widget.rejected.connect(self.app_close)
        return self.app.exec_()

    def on_mode_selected(self, result):
        print("Result: {}".format(result))
        self.user_info_widget = UserDataInput(self.controller)
        self.user_info_widget.show()
        self.user_info_widget.accepted.connect(self.on_user_data_entered)
        self.user_info_widget.rejected.connect(self.app_close)
        pass

    def app_close(self):
        self.app.quit()

    def on_user_data_entered(self):
        pass
