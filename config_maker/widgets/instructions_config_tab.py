from PyQt5.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout



class InstructionsConfigTab(QWidget):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        ig_instructions = QTextEdit()
        ig_instructions_label = QLabel(
            "Before interval generation training session:")

        ig_pre_measuring = QTextEdit()
        ig_pre_measuring_label = QLabel(
            "Before interval generation measuring session:")

        igns_instructions = QTextEdit()
        igns_instructions_label = QLabel(
            "Before interval generation with card selection training session:")

        thanks_text = QTextEdit()
        thanks_text_label = QLabel("Thank-you text:")

        vbox = QVBoxLayout()
        vbox.addWidget(ig_instructions_label)
        vbox.addWidget(ig_instructions)
        vbox.addSpacing(15)
        vbox.addWidget(ig_pre_measuring_label)
        vbox.addWidget(ig_pre_measuring)
        vbox.addSpacing(15)
        vbox.addWidget(igns_instructions_label)
        vbox.addWidget(igns_instructions)
        vbox.addSpacing(15)
        vbox.addWidget(thanks_text_label)
        vbox.addWidget(thanks_text)

        self.setLayout(vbox)
