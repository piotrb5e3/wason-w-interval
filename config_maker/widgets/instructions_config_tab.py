from PyQt5.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout


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
            "Before the main experiment in control group "
            "(Also shown in pilot mode):")

        main_exp_click_instructions = QTextEdit()
        main_exp_click_instructions.setText(
            self.controller.get_pre_exp_w_click_instr())
        connect(main_exp_click_instructions,
                self.controller.set_pre_exp_w_click_instr)
        main_exp_click_instructions_label = QLabel(
            "Before the main experiment in experiment groups:")

        thanks_text = QTextEdit()
        thanks_text.setText(self.controller.get_thanks_text())
        connect(thanks_text, self.controller.set_thanks_text)
        thanks_text_label = QLabel("Thank-you text:")

        vbox = QVBoxLayout()
        vbox.addWidget(ig_instructions_label)
        vbox.addWidget(ig_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(ig_pre_measuring_label)
        vbox.addWidget(ig_pre_measuring)
        vbox.addSpacing(15)
        vbox.addWidget(igns_instructions_label)
        vbox.addWidget(igns_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(main_exp_instructions_label)
        vbox.addWidget(main_exp_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(main_exp_click_instructions_label)
        vbox.addWidget(main_exp_click_instructions)
        vbox.addSpacing(5)
        vbox.addWidget(thanks_text_label)
        vbox.addWidget(thanks_text)

        self.setLayout(vbox)
