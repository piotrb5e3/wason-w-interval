from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

INTEGER_REGEXP = QRegExp('[1-9][0-9]*')


class ExperimentConfigTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        training_time = QLineEdit()
        numeric_validator = QRegExpValidator(INTEGER_REGEXP, training_time)
        training_time.setValidator(numeric_validator)
        training_time.setText(str(self.controller.get_training_session_time()))
        training_time.textEdited.connect(
            self.controller.set_training_session_time)
        training_time_label = QLabel(
            "Interval generation training session length (sec):")

        measuring_time = QLineEdit()
        numeric_validator = QRegExpValidator(INTEGER_REGEXP, measuring_time)
        measuring_time.setValidator(numeric_validator)
        measuring_time.setText(
            str(self.controller.get_measuring_session_time()))
        measuring_time.textEdited.connect(
            self.controller.set_measuring_session_time)
        measuring_time_label = QLabel(
            "Interval generation measuring session length (sec):")

        selection_training_time = QLineEdit()
        numeric_validator = QRegExpValidator(INTEGER_REGEXP,
                                             selection_training_time)
        selection_training_time.setValidator(numeric_validator)
        selection_training_time.setText(
            str(self.controller.get_selection_training_session_time()))
        selection_training_time.textEdited.connect(
            self.controller.set_selection_training_session_time)
        selection_training_time_label = QLabel(
            "Interval generation and card selection training "
            "session length (sec):"
        )

        nc_timeout = QLineEdit()
        numeric_validator = QRegExpValidator(INTEGER_REGEXP, nc_timeout)
        nc_timeout.setValidator(numeric_validator)
        nc_timeout.setText(str(self.controller.get_no_clicking_warning_time()))
        nc_timeout.textEdited.connect(
            self.controller.set_no_clicking_warning_time)
        nc_timeout_label = QLabel(
            "The no-clicking-warning-timeout value (sec):"
        )

        vbox = QVBoxLayout()
        vbox.addWidget(training_time_label)
        vbox.addWidget(training_time)
        vbox.addSpacing(20)
        vbox.addWidget(measuring_time_label)
        vbox.addWidget(measuring_time)
        vbox.addSpacing(20)
        vbox.addWidget(selection_training_time_label)
        vbox.addWidget(selection_training_time)
        vbox.addSpacing(20)
        vbox.addWidget(nc_timeout_label)
        vbox.addWidget(nc_timeout)
        vbox.addStretch()

        self.setLayout(vbox)
