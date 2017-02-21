from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QVBoxLayout)


class CSCardsEditTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        def nth_card_setter(n):
            return lambda t: self.controller.set_nth_card_text(n, t)

        vbox = QVBoxLayout()
        for i in range(4):
            l = QLabel("Card #{}".format(i + 1))
            vbox.addWidget(l)
            e = QLineEdit()
            e.setText(self.controller.get_nth_card_text(i))
            e.textEdited.connect(nth_card_setter(i))
            vbox.addWidget(e)

        vbox.addStretch()

        self.setLayout(vbox)
