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
        self.current_screen = Instructions("Before clicking training session")
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_clicking_training_session)

    def show_clicking_training_session(self):
        click_controller = self.controller.get_click_training_controller()
        self.current_screen = TimedIntervalInput(
            click_controller, self.controller.get_click_training_time())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.show_2nd_instructions)

    def show_2nd_instructions(self):
        self.current_screen = Instructions("After clicking training session "
                                           "before clicking measuring session")
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_clicking_measuring_session)

    def show_clicking_measuring_session(self):
        click_controller = self.controller.get_click_measuring_controller()
        self.current_screen = TimedIntervalInput(
            click_controller, self.controller.get_click_measuring_time())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.show_3rd_instructions)

    def show_3rd_instructions(self):
        self.current_screen = Instructions("After clicking measuring session")
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_next_selection_experiment)

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
        self.current_screen = Instructions("Thank you page")
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.close)
