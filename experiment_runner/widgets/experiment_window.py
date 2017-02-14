from PyQt5.QtWidgets import (QMainWindow, QGridLayout)

from .experiment_screens import Instructions, TimedIntervalInput


class ExperimentWindow(QMainWindow):
    controller = None
    current_screen = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.show_initial_instructions()

    def show_initial_instructions(self):
        self.current_screen = Instructions("Hello World!")
        self.setCentralWidget(self.current_screen)
        self.current_screen.accepted.connect(self.show_2nd_instructions)

    def show_2nd_instructions(self):
        self.current_screen = Instructions("But wait, there's more!")
        self.setCentralWidget(self.current_screen)
        self.current_screen.accepted.connect(self.show_clicking_training_session)

    def show_clicking_training_session(self):
        self.current_screen = TimedIntervalInput(self.controller, 10000)
        self.setCentralWidget(self.current_screen)
        self.current_screen.accepted.connect(self.close)
