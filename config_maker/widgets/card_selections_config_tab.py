from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QVBoxLayout,
                             QPushButton, QHBoxLayout)

from .card_selection_edit import CardSelectionEdit


class CardSelectionsConfigTab(QWidget):
    controller = None
    list = None
    list_items = None
    edit = None
    current_editor = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.list = QListWidget()
        self.list_items = []

        add = QPushButton("Add")
        add.clicked.connect(self.show_add_dialog)

        self.edit = QPushButton("Edit")
        self.edit.setEnabled(False)

        hbox = QHBoxLayout()
        hbox.addWidget(add)
        hbox.addWidget(self.edit)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list)
        vbox.addLayout(hbox)

        self.reload_items()

        self.setLayout(vbox)

    def reload_items(self):
        for l in self.list_items:
            self.list.removeItemWidget(l)

        self.list_items = []
        for c in self.controller.get_cs_controllers():
            list_item = QListWidgetItem(
                "{} - {}".format(
                    c.get_rule(),
                    "Training" if c.is_fixed_position() else "Experiment"))
            self.list.addItem(list_item)
            self.list_items.append(list_item)

    def show_add_dialog(self):
        self.current_editor = CardSelectionEdit()
        self.current_editor.accepted.connect(self.reload_items)
        self.current_editor.show()
