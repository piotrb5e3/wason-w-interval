from PyQt5.QtWidgets import QDialog, QTabWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from .card_selection_text_edit import CSTextEditTab
from .card_selection_cards_edit import CSCardsEditTab


class CardSelectionEdit(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.init_ui()

    def init_ui(self):
        tabs = QTabWidget()
        tabs.addTab(CSTextEditTab(), "Text")
        tabs.addTab(CSCardsEditTab(), "Cards")
        save = QPushButton("Accept")

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(save, Qt.AlignRight)
        
        self.setLayout(vbox)
