from PyQt5.QtWidgets import (QWidget, QHBoxLayout)

from .experiment_screens import Instructions, TimedIntervalInput, CardSelect


class ExperimentWindow(QWidget):
    controller = None
    current_screen = None
    layout = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.show_initial_instructions()

    def show_initial_instructions(self):
        self.current_screen = Instructions(
            self.controller.get_interval_instructions_text())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_clicking_training_session)

    def show_clicking_training_session(self):
        click_controller = self.controller.get_click_training_controller()
        self.current_screen = TimedIntervalInput(
            click_controller, self.controller.get_click_training_time())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.show_measuring_session_instr)

    def show_measuring_session_instr(self):
        self.current_screen = Instructions(
            self.controller.get_interval_pre_measurement_text())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_clicking_measuring_session)

    def show_clicking_measuring_session(self):
        click_controller = self.controller.get_click_measuring_controller()
        self.current_screen = TimedIntervalInput(
            click_controller, self.controller.get_click_measuring_time())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_selection_training_session_instr)

    def show_selection_training_session_instr(self):
        self.current_screen = Instructions(
            self.controller.get_selection_training_instructions_text())
        self.layout.addWidget(self.current_screen)
        if self.controller.has_more_experiments():
            self.current_screen.accepted.connect(
                self.show_next_selection_experiment)
        else:
            self.current_screen.accepted.connect(self.show_thank_you_page)

    def show_next_selection_experiment(self):
        clickc, cardc = self.controller.get_next_click_card_controllers()
        self.current_screen = CardSelect(cardc, clickc)
        self.layout.addWidget(self.current_screen)
        if self.controller.has_more_experiments():
            self.current_screen.accepted.connect(
                self.show_next_selection_experiment)
        else:
            self.current_screen.accepted.connect(self.show_thank_you_page)

    def show_thank_you_page(self):
        self.current_screen = Instructions(self.controller.get_thank_you_text())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.close)
