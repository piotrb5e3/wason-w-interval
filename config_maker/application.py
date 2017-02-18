from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QMainWindow, QTabWidget,
                             QPushButton, QWidget, QFileDialog)

from controller import ConfigController
from widgets import (NewOrLoad, ExperimentConfigTab, CardSelectionsConfigTab,
                     InstructionsConfigTab)

ALIGN_RIGHT = 0x0002


class Application(object):
    new_or_load = None
    main_window = None
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
        cs_conf = CardSelectionsConfigTab(self.controller)
        instr_conf = InstructionsConfigTab(self.controller)
        exp_conf = ExperimentConfigTab(self.controller)

        tabs = QTabWidget()
        tabs.addTab(exp_conf, "Basic")
        tabs.addTab(instr_conf, "Instructions")
        tabs.addTab(cs_conf, "Cards")

        save = QPushButton("Save")
        save.clicked.connect(self.on_save)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(save, alignment=Qt.AlignRight)

        wrap = QWidget()
        wrap.setLayout(vbox)

        self.main_window = QMainWindow()
        self.main_window.setCentralWidget(wrap)
        self.main_window.setGeometry(300, 200, 500, 700)
        self.main_window.show()

    def on_save(self):
        errors = self.controller.get_errors_list()
        if errors:
            pass
        else:
            fname = QFileDialog.getSaveFileName(
                self.main_window,
                'Save as',
                filter='Experiment Configuration (*.conf)')

            fname = fname[0]

            if not fname:
                return

            if not fname.endswith('.conf'):
                fname += '.conf'
            if self.controller.save(fname):
                self.app.quit()
