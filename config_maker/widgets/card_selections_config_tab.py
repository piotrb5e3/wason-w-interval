from PyQt5.QtWidgets import (QWidget, QListWidget, QListWidgetItem, QVBoxLayout,
                             QPushButton, QHBoxLayout, QAbstractItemView)

from .card_selection_edit import CardSelectionEdit


class CardSelectionsConfigTab(QWidget):
    controller = None
    list = None
    list_items = None
    edit = None
    up = None
    down = None
    delete = None
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

        self.delete = QPushButton("Delete")
        self.delete.setEnabled(False)
        self.delete.clicked.connect(self.delete_selected)

        self.up = QPushButton("Move up")
        self.up.setEnabled(False)
        self.up.clicked.connect(self.move_up)

        self.down = QPushButton("Move Down")
        self.down.setEnabled(False)
        self.down.clicked.connect(self.move_down)

        hbox = QHBoxLayout()
        hbox.addWidget(add)
        hbox.addWidget(self.edit)
        hbox.addWidget(self.delete)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.up)
        hbox2.addWidget(self.down)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch()

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
        n = -1
        for i in range(len(self.list_items)):
            if self.list_items[i].isSelected():
                n = i
                break
        ctrl = self.controller.get_edit_cs_controller(n)
        self.current_editor = CardSelectionEdit(ctrl)
        self.current_editor.accepted.connect(self.reload_items)
        self.current_editor.show()

    def delete_selected(self):
        n = -1
        for i in range(len(self.list_items)):
            if self.list_items[i].isSelected():
                n = i
                break
        self.controller.delete_nth_cs(n)
        self.reload_items()

    def move_up(self):
        n = -1
        for i in range(len(self.list_items)):
            if self.list_items[i].isSelected():
                n = i
                break
        self.controller.move_up(n)
        self.reload_items()

    def move_down(self):
        n = -1
        for i in range(len(self.list_items)):
            if self.list_items[i].isSelected():
                n = i
                break
        self.controller.move_down(n)
        self.reload_items()

    def update_edit_button_state(self):
        if len(self.list.selectedItems()) > 0:
            self.edit.setEnabled(True)
            self.delete.setEnabled(True)
            self.up.setEnabled(True)
            self.down.setEnabled(True)
        else:
            self.edit.setEnabled(False)
            self.delete.setEnabled(False)
            self.up.setEnabled(False)
            self.down.setEnabled(False)
