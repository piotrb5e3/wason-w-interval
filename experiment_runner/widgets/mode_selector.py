from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QVBoxLayout, QMessageBox, QDialog)

from experiment_runner.controller import MODES


class ModeSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def finish_wrapper(val):
            def fin():
                self.done(val)

            return fin

        self.setWindowTitle('Select mode')

        b1 = QPushButton('Group without feedback', self)
        b1.clicked.connect(finish_wrapper(MODES['NO_FEEDBACK_EXPERIMENT']))

        b2 = QPushButton('Group with feedback', self)
        b2.clicked.connect(finish_wrapper(MODES['FEEDBACK_EXPERIMENT']))

        b3 = QPushButton('Control group', self)
        b3.clicked.connect(finish_wrapper(MODES['CONTROL_GROUP']))

        b4 = QPushButton('Pilot mode', self)
        b4.clicked.connect(finish_wrapper(MODES['PILOT']))

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(b1)
        vbox.addWidget(b2)
        vbox.addWidget(b3)
        vbox.addWidget(b4)

        self.setLayout(vbox)
        self.setMinimumWidth(400)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            self.reject()
        else:
            event.ignore()
