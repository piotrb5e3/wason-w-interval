from PyQt5.QtWidgets import (QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QFrame, QComboBox)
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator
from dialog import UnrejectableDialog


class UserDataInput(UnrejectableDialog):
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
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)
        frame.setFixedSize(1200, 700)

        header = QLabel('User information')

        name_label = QLabel('Name or alias:')
        sex_label = QLabel('Sex:')
        age_label = QLabel('Age:')

        self.name = QLineEdit()
        name_validator = QRegExpValidator(QRegExp('.+'), self.name)
        self.name.setValidator(name_validator)

        self.sex = QComboBox()
        self.sex.addItem("------")
        self.sex.addItem("Male")
        self.sex.addItem("Female")

        self.age = QLineEdit()
        age_validator = QRegExpValidator(QRegExp('[1-9][0-9]*'), self.age)
        self.age.setValidator(age_validator)

        self.next = QPushButton("Continue")
        self.next.setEnabled(False)

        self.name.textChanged.connect(self.on_change)
        self.sex.currentTextChanged.connect(self.on_change)
        self.age.textChanged.connect(self.on_change)
        self.next.pressed.connect(self.on_submit)

        vbox = QVBoxLayout()
        vbox.addStretch()
        vbox.addWidget(header, alignment=Qt.AlignCenter)
        vbox.addWidget(name_label)
        vbox.addWidget(self.name)
        vbox.addWidget(sex_label)
        vbox.addWidget(self.sex)
        vbox.addWidget(age_label)
        vbox.addWidget(self.age)
        vbox.addStretch()
        vbox.addWidget(self.next, alignment=Qt.AlignRight)

        frame.setLayout(vbox)
        framebox = QVBoxLayout()
        framebox.addWidget(frame, alignment=Qt.AlignCenter)
        self.setLayout(framebox)

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
