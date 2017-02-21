from PyQt5.QtWidgets import (QDialog, QTabWidget, QPushButton, QVBoxLayout,
                             QMessageBox)
from PyQt5.QtCore import Qt
from .card_selection_text_edit import CSTextEditTab
from .card_selection_cards_edit import CSCardsEditTab


class CardSelectionEdit(QDialog):
    controller = None
    msg = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setModal(True)
        self.init_ui()

    def init_ui(self):
        tabs = QTabWidget()
        tabs.addTab(CSTextEditTab(self.controller), "Text")
        tabs.addTab(CSCardsEditTab(self.controller), "Cards")
        save = QPushButton("Accept")
        save.clicked.connect(self.accept_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(save, alignment=Qt.AlignRight)

        self.setLayout(vbox)

    def accept_clicked(self):
        if not self.controller.get_rule():
            self.msg = QMessageBox(self)
            self.msg.setText("No rule defined")
            self.msg.setBaseSize(300, 200)
            self.msg.show()
            return

        self.controller.save()
        self.accept()
