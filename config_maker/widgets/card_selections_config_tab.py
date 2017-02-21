from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QVBoxLayout,
                             QPushButton, QHBoxLayout, QAbstractItemView)

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
        self.list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.list.itemSelectionChanged.connect(self.update_edit_button_state)
        self.list_items = []

        add = QPushButton("Add")
        add.clicked.connect(self.show_add_dialog)

        self.edit = QPushButton("Edit")
        self.edit.setEnabled(False)
        self.edit.clicked.connect(self.show_edit_dialog)

        hbox = QHBoxLayout()
        hbox.addWidget(add)
        hbox.addWidget(self.edit)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list)
        vbox.addLayout(hbox)

        self.reload_items()

        self.setLayout(vbox)

    def reload_items(self):
        self.list.clear()

        self.list_items = []
        for c in self.controller.get_cs_controllers():
            list_item = QListWidgetItem(
                "{} - {}".format(
                    c.get_rule(),
                    "Training" if c.is_fixed_position() else "Experiment"))
            self.list.addItem(list_item)
            self.list_items.append(list_item)
        self.list.update()

    def show_add_dialog(self):
        ctrl = self.controller.get_add_cs_controller()
        self.current_editor = CardSelectionEdit(ctrl)
        self.current_editor.accepted.connect(self.reload_items)
        self.current_editor.show()

    def show_edit_dialog(self):
        n = 0
        for i in range(len(self.list_items)):
            if self.list_items[i].isSelected():
                n = i
                break
        ctrl = self.controller.get_edit_cs_controller(n)
        self.current_editor = CardSelectionEdit(ctrl)
        self.current_editor.accepted.connect(self.reload_items)
        self.current_editor.show()

    def update_edit_button_state(self):
        if len(self.list.selectedItems()) > 0:
            self.edit.setEnabled(True)
        else:
            self.edit.setEnabled(False)
