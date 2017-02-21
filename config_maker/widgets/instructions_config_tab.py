from PyQt5.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout, QLineEdit


class InstructionsConfigTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        def connect(text_edit, c_fun):
            text_edit.textChanged.connect(
                lambda: c_fun(text_edit.toPlainText()))

        welcome = QLineEdit()
        welcome.setText(self.controller.get_welcome_text())
        welcome.textEdited.connect(self.controller.set_welcome_text)
        welcome_label = QLabel("Welcome text:")

        ig_instructions = QTextEdit()
        ig_instructions.setText(self.controller.get_ig_instr())
        connect(ig_instructions, self.controller.set_ig_instr)
        ig_instructions_label = QLabel(
            "Before interval generation training session:")

        ig_pre_measuring = QTextEdit()
        ig_pre_measuring.setText(self.controller.get_ig_measuring_instr())
        connect(ig_pre_measuring, self.controller.set_ig_measuring_instr)
        ig_pre_measuring_label = QLabel(
            "Before interval generation measuring session:")

        igns_instructions = QTextEdit()
        igns_instructions.setText(self.controller.get_ig_w_cs_training_instr())
        connect(igns_instructions, self.controller.set_ig_w_cs_training_instr)
        igns_instructions_label = QLabel(
            "Before interval generation with card selection training session:")

        main_exp_instructions = QTextEdit()
        main_exp_instructions.setText(self.controller.get_pre_exp_instr())
        connect(main_exp_instructions, self.controller.set_pre_exp_instr)
        main_exp_instructions_label = QLabel(
            "Before the main experiment (Also shown in pilot mode):")

        short_instr = QLineEdit()
        short_instr.setText(self.controller.get_short_instr())
        short_instr.textEdited.connect(self.controller.set_short_instr)
        short_instr_label = QLabel(
            "Short instructions (shown below cards on the selection screen):")

        thanks_text = QTextEdit()
        thanks_text.setText(self.controller.get_thanks_text())
        connect(thanks_text, self.controller.set_thanks_text)
        thanks_text_label = QLabel("Thank-you text:")

        vbox = QVBoxLayout()
        vbox.addWidget(welcome_label)
        vbox.addWidget(welcome)
        vbox.addSpacing(5)
        vbox.addWidget(ig_instructions_label)
        vbox.addWidget(ig_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(ig_pre_measuring_label)
        vbox.addWidget(ig_pre_measuring)
        vbox.addSpacing(5)
        vbox.addWidget(igns_instructions_label)
        vbox.addWidget(igns_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(main_exp_instructions_label)
        vbox.addWidget(main_exp_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(short_instr_label)
        vbox.addWidget(short_instr)
        vbox.addSpacing(5)
        vbox.addWidget(thanks_text_label)
        vbox.addWidget(thanks_text)

        self.setLayout(vbox)
