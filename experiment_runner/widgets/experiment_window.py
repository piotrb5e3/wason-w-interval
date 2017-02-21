from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QMessageBox)

from .experiment_screens import (Instructions, TimedIntervalInput, CardSelect,
                                 CardSelectionTraining)


class ExperimentWindow(QWidget):
    controller = None
    current_screen = None
    layout = None
    can_close = False
    expno = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.expno = 1
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
        self.current_screen.accepted.connect(
            self.show_selection_training)

    def show_selection_training(self):
        click_controller = self.controller.get_click_training_controller()
        self.current_screen = CardSelectionTraining(
            click_controller, self.controller.get_selection_training_time())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_main_experiment_instructions)

    def show_main_experiment_instructions(self):
        self.current_screen = Instructions(
            self.controller.get_main_experiment_instructions_text())
        self.layout.addWidget(self.current_screen)
        if self.controller.has_more_experiments():
            self.current_screen.accepted.connect(
                self.show_break_screen)
        else:
            self.current_screen.accepted.connect(self.show_thank_you_page)

    def show_break_screen(self):
        self.current_screen = Instructions("Experiment {}".format(self.expno))
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(
            self.show_next_selection_experiment)
        self.expno += 1

    def show_next_selection_experiment(self):
        clickc, cardc = self.controller.get_next_click_card_controllers()
        self.current_screen = CardSelect(cardc, clickc)
        self.layout.addWidget(self.current_screen)
        if self.controller.has_more_experiments():
            self.current_screen.accepted.connect(
                self.show_break_screen)
        else:
            self.current_screen.accepted.connect(self.show_thank_you_page)

    def show_thank_you_page(self):
        self.current_screen = Instructions(self.controller.get_thank_you_text())
        self.layout.addWidget(self.current_screen)
        self.current_screen.accepted.connect(self.end_experiment)

    def end_experiment(self):
        self.can_close = True
        self.close()

    def closeEvent(self, event):
        if self.can_close:
            event.accept()
            return

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
