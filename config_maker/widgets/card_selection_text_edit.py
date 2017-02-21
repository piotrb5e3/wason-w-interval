from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QVBoxLayout, QLineEdit)


class CSTextEditTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        def connect(text_edit, c_fun):
            text_edit.textChanged.connect(
                lambda: c_fun(text_edit.toPlainText()))

        vbox = QVBoxLayout()

        txt_label = QLabel("Task text:")
        vbox.addWidget(txt_label)
        txt = QTextEdit()
        txt.setText(self.controller.get_task_text())
        connect(txt, self.controller.set_task_text)
        vbox.addWidget(txt)

        rule_label = QLabel("Rule text:")
        vbox.addWidget(rule_label)
        rule = QLineEdit()
        rule.setText(self.controller.get_rule())
        rule.textEdited.connect(self.controller.set_rule)
        vbox.addWidget(rule)

        txt_extra_label = QLabel("Extra task text (shown below the rule):")
        vbox.addWidget(txt_extra_label)
        txt_extra = QTextEdit()
        txt_extra.setText(self.controller.get_extra_text())
        connect(txt_extra, self.controller.set_extra_text)
        vbox.addWidget(txt_extra)

        instr_label = QLabel("Task instructions (shown below cards):")
        vbox.addWidget(instr_label)
        instr = QTextEdit()
        instr.setText(self.controller.get_instructions())
        connect(instr, self.controller.set_instructions)
        vbox.addWidget(instr)

        self.setLayout(vbox)
