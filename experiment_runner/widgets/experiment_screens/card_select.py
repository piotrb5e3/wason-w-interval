from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QPushButton, QLabel,
                             QVBoxLayout, QWidget)
from PyQt5.QtCore import QTimer, Qt, QMargins
from PyQt5.QtGui import QPalette, QColor, QFont, QPainter

from .interval_input import IntervalInput

from dialog import UnrejectableDialog
from .text_field import WrappingTextField

S_TO_MS = 1000


class CardSelect(UnrejectableDialog):
    card_controller = None
    click_controller = None
    layout = None

    def __init__(self, card_controller, click_controller):
        super().__init__()
        self.card_controller = card_controller
        self.click_controller = click_controller
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()
        screen1 = CardSelectScreenOne(self.card_controller)
        screen1.accepted.connect(self.selection_start)
        self.layout.addWidget(screen1)
        self.setLayout(self.layout)

    def selection_start(self):
        screen2 = CardSelectScreenTwo(self.card_controller,
                                      self.click_controller)
        screen2.accepted.connect(self.accept)
        self.layout.addWidget(screen2)


class CardSelectScreenOne(UnrejectableDialog):
    card_controller = None

    def __init__(self, card_controller):
        super().__init__()
        self.card_controller = card_controller
        self.card_controller.start()
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)
        frame.setFixedSize(1200, 700)

        next = QPushButton("Continue")
        next.clicked.connect(self.accept)

        t1box = WrappingTextField(self.card_controller.get_t1())
        card_placeholder = QWidget()
        card_placeholder.setMinimumHeight(120)
        selection_specific_instr_placeholder = WrappingTextField("")
        short_instr_placeholder = WrappingTextField("")

        if self.card_controller.show_all_at_once():
            rulebox = WrappingTextField(self.card_controller.get_rule())
            t2box = WrappingTextField(self.card_controller.get_t2())
        else:
            rulebox = WrappingTextField("")
            t2box = WrappingTextField("")

        vbox = QVBoxLayout()
        vbox.addWidget(t1box)
        vbox.addWidget(rulebox)
        vbox.addWidget(t2box)
        vbox.addWidget(card_placeholder)
        vbox.addWidget(selection_specific_instr_placeholder)
        vbox.addWidget(short_instr_placeholder)
        vbox.addWidget(next, alignment=Qt.AlignRight)
        frame.setLayout(vbox)

        box = QHBoxLayout()
        box.addWidget(frame)
        self.setLayout(box)


class CardSelectScreenTwo(UnrejectableDialog):
    card_controller = None
    click_controller = None
    cards = None

    def __init__(self, card_controller, click_controller):
        super().__init__()
        self.card_controller = card_controller
        self.click_controller = click_controller
        self.init_ui()
        self.click_controller.start()
        self.card_controller.solving_start()

    def init_ui(self):
        def on_click_btn_no(n):
            return lambda: self.card_controller.on_click(n)

        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)
        frame.setFixedSize(1200, 700)

        next = QPushButton("Continue")
        next.clicked.connect(self.selection_finish)

        t1box = WrappingTextField(self.card_controller.get_t1())
        rulebox = WrappingTextField(self.card_controller.get_rule())
        t2box = WrappingTextField(self.card_controller.get_t2())
        i1box = WrappingTextField(self.card_controller.get_i1())
        i2box = WrappingTextField(self.card_controller.get_i2())

        cards_layout = QHBoxLayout()
        self.cards = []
        texts = self.card_controller.get_card_texts()
        for i in range(4):
            b = CardButton(texts[i])
            b.clicked.connect(on_click_btn_no(i + 1))
            self.cards.append(b)
            cards_layout.addWidget(b)

        vbox = QVBoxLayout()
        vbox.addWidget(t1box)
        vbox.addWidget(rulebox)
        vbox.addWidget(t2box)
        vbox.addLayout(cards_layout)
        vbox.addWidget(i1box)
        vbox.addWidget(i2box)
        vbox.addWidget(next, alignment=Qt.AlignRight)

        frame.setLayout(vbox)

        box = QHBoxLayout()
        box.addWidget(frame)
        interval_input = IntervalInput(self.click_controller)
        interval_input.setLayout(box)

        box2 = QHBoxLayout()
        box2.addWidget(interval_input)
        box2.setContentsMargins(0, 0, 0, 0)

        self.setLayout(box2)

    def selection_finish(self):
        is_selected_list = [btn.isChecked() for btn in self.cards]
        self.card_controller.end(is_selected_list)
        self.accept()


class CardSelectionTraining(UnrejectableDialog):
    click_controller = None
    timeout = None

    def __init__(self, click_controller, timeout_in_sec):
        super().__init__()
        self.click_controller = click_controller
        self.click_controller.start()
        self.timeout = QTimer.singleShot(timeout_in_sec * S_TO_MS,
                                         self.accept)
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)
        frame.setFixedSize(1200, 700)

        t1box = QLabel("")
        rulebox = QLabel("")
        t2box = QLabel("")
        i1box = QLabel("")
        i2box = QLabel("")

        cards_layout = QHBoxLayout()
        for i in range(4):
            b = CardButton("")
            cards_layout.addWidget(b)

        vbox = QVBoxLayout()
        vbox.addWidget(t1box)
        vbox.addWidget(rulebox)
        vbox.addWidget(t2box)
        vbox.addLayout(cards_layout)
        vbox.addWidget(i1box)
        vbox.addWidget(i2box)

        frame.setLayout(vbox)

        box = QHBoxLayout()
        box.addWidget(frame)
        interval_input = IntervalInput(self.click_controller)
        interval_input.setLayout(box)

        box2 = QHBoxLayout()
        box2.addWidget(interval_input)
        box2.setContentsMargins(0, 0, 0, 0)

        self.setLayout(box2)


class CardButton(QPushButton):
    normal_palette = None
    pushed_palette = None
    txt = None

    def __init__(self, text):
        super().__init__("")
        self.txt = text
        self.setCheckable(True)
        self.setMinimumHeight(120)
        self.normal_palette = self.palette()
        self.pushed_palette = QPalette(self.normal_palette)
        self.pushed_palette.setColor(QPalette.Button, QColor(144, 151, 249))
        self.toggled.connect(self.on_toggle)

    def on_toggle(self, is_toggled):
        if is_toggled:
            self.setPalette(self.pushed_palette)
        else:
            self.setPalette(self.normal_palette)
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter()
        qp.begin(self)
        self.draw_text(event, qp)
        qp.end()

    def draw_text(self, event, qp):
        draw_rect = event.rect().marginsRemoved(QMargins(5, 5, 5, 5))
        qp.setPen(QColor(0, 0, 0))
        qp.setFont(QFont('Serif', 11))
        qp.drawText(draw_rect, Qt.TextWordWrap | Qt.AlignLeft, self.txt)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.RightButton:
            event.accept()
