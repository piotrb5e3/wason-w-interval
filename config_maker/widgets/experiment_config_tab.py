from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QVBoxLayout


class ExperimentConfigTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        training_time = QLineEdit()
        training_time_label = QLabel(
            "Interval generation training session length (sec):")

        measuring_time = QLineEdit()
        measuring_time_label = QLabel(
            "Interval generation measuring session length (sec):")

        selection_training_time = QLineEdit()
        selection_training_time_label = QLabel(
            "Interval generation and card selection training "
            "session length (sec):"
        )

        nc_timeout = QLineEdit()
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
