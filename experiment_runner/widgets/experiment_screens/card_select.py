from PyQt5.QtWidgets import (QDialog, QFrame, QGridLayout, QHBoxLayout,
                             QPushButton, QLabel)

from .interval_input import IntervalInput


class CardSelect(QDialog):
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


class CardSelectScreenOne(QDialog):
    card_controller = None

    def __init__(self, card_controller):
        super().__init__()
        self.card_controller = card_controller
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)

        next = QPushButton("Continue")
        next.clicked.connect(self.accept)

        t1box = QLabel(self.card_controller.get_t1())
        rulebox = QLabel(self.card_controller.get_rule())
        t2box = QLabel(self.card_controller.get_t2())
        grid = QGridLayout()
        grid.addWidget(t1box, 0, 0, 4, 0)
        if self.card_controller.show_all_at_once():

            grid.addWidget(rulebox, 0, 1, 4, 1)
            grid.addWidget(t2box, 0, 2, 4, 2)
            grid.addWidget(next, 4, 3)
        else:
            grid.addWidget(next, 4, 1)

        frame.setLayout(grid)

        box = QHBoxLayout()
        box.addWidget(frame)
        box.setContentsMargins(300, 100, 300, 100)
        self.setLayout(box)


class CardSelectScreenTwo(QDialog):
    card_controller = None
    click_controller = None
    cards = None

    def __init__(self, card_controller, click_controller):
        super().__init__()
        self.card_controller = card_controller
        self.click_controller = click_controller
        self.init_ui()

    def init_ui(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel)
        frame.setLineWidth(1)

        next = QPushButton("Continue")
        next.clicked.connect(self.selection_finish)

        t1box = QLabel(self.card_controller.get_t1())
        rulebox = QLabel(self.card_controller.get_rule())
        t2box = QLabel(self.card_controller.get_t2())
        i1box = QLabel(self.card_controller.get_i1())
        i2box = QLabel(self.card_controller.get_i2())

        cards_layout = QHBoxLayout()
        self.cards = []
        for t in self.card_controller.get_card_texts():
            b = QPushButton(t)
            b.setCheckable(True)
            self.cards.append(b)
            cards_layout.addWidget(b)

        grid = QGridLayout()

        grid.addWidget(t1box, 0, 0, 4, 0)
        grid.addWidget(rulebox, 0, 1, 4, 1)
        grid.addWidget(t2box, 0, 2, 4, 2)
        grid.addChildLayout(cards_layout)
        grid.addWidget(i1box, 0, 4, 4, 4)
        grid.addWidget(i2box, 0, 5, 4, 5)
        grid.addWidget(next, 4, 6)

        frame.setLayout(grid)

        box = QHBoxLayout()
        box.addWidget(frame)
        box.setContentsMargins(300, 100, 300, 100)
        interval_input = IntervalInput(self.click_controller)
        interval_input.setLayout(box)

        box2 = QHBoxLayout()
        box2.addWidget(interval_input)

        self.setLayout(box2)

    def selection_finish(self):
        is_selected_list = [btn.is_checked() for btn in self.cards]
        self.card_controller.end(is_selected_list)
        self.accept()
