from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton,
                             QGridLayout, QVBoxLayout, QMessageBox, QDialog,
                             QComboBox
                             )
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class UserDataInput(QDialog):
    controller = None
    name = None
    age = None
    sex = None
    next = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User information')

        name_label = QLabel('Name')
        sex_label = QLabel('Sex')
        age_label = QLabel('Age')

        self.name = QLineEdit()
        name_validator = QRegExpValidator(QRegExp('[a-zA-Z].*'), self.name)
        self.name.setValidator(name_validator)

        self.sex = QComboBox()
        self.sex.addItem("------")
        self.sex.addItem("Male")
        self.sex.addItem("Female")

        self.age = QLineEdit()
        age_validator = QRegExpValidator(QRegExp('[1-9][0-9]*'), self.age)
        self.age.setValidator(age_validator)

        self.next = QPushButton("OK")
        self.next.setEnabled(False)

        self.name.textChanged.connect(self.on_change)
        self.sex.currentTextChanged.connect(self.on_change)
        self.age.textChanged.connect(self.on_change)
        self.next.pressed.connect(self.on_submit)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name, 0, 1)
        grid.addWidget(sex_label, 1, 0)
        grid.addWidget(self.sex, 1, 1)
        grid.addWidget(age_label, 2, 0)
        grid.addWidget(self.age, 2, 1)

        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addLayout(grid)
        vbox.addWidget(self.next)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 280, 170)

    def on_change(self):
        name, sex, age = self.extract_user_info()
        if age < 1 or age > 200:
            self.next.setEnabled(False)
            return
        if not name:
            self.next.setEnabled(False)
            return
        if sex not in ('Male', 'Female'):
            self.next.setEnabled(False)
            return
        self.next.setEnabled(True)

    def on_submit(self):
        name, sex, age = self.extract_user_info()
        if age < 1 or age > 200:
            return
        if not name:
            return
        if sex not in ('Male', 'Female'):
            return
        self.controller.submit_user_data(name=name, sex=sex, age=age)
        self.accept()

    def extract_user_info(self):
        try:
            name = self.name.text()
            age = int(self.age.text())
            sex = self.sex.currentText()
        except ValueError:
            return None, None, 0
        return name, sex, age

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

    class UserDataException(Exception):
        pass
