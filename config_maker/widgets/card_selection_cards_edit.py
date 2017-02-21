from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout)


class CSCardsEditTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()
        for i in range(4):
            l = QLabel("Card #{}".format(i + 1))
            vbox.addWidget(l)
            e = QLineEdit()
            e.setText(self.controller.get_nth_card_text(i))
            e.textEdited.connect(
                lambda t: self.controller.set_nth_card_text(i, t))
            vbox.addWidget(e)

        vbox.addStretch()

        self.setLayout(vbox)
