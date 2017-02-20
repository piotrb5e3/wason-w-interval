from time import time
from random import shuffle


class CardController(object):
    storage = None
    card_selection = None
    is_recording = None
    expno = None
    shuffled_cards = None
    start_time = None

    def __init__(self, storage, card_selection, is_recording, expno):
        self.storage = storage
        self.card_selection = card_selection
        self.is_recording = is_recording
        self.expno = expno
        self.shuffled_cards = list(self.card_selection.cards)
        shuffle(self.shuffled_cards)

    def show_all_at_once(self):
        return False

    def start(self):
        self.start_time = time()

    def end(self, is_pushed_list):
        time_delta = time() - self.start_time

        positions = {}
        status = {}

        for i in range(4):
            n = self.shuffled_cards[i].number
            positions[n] = i
            status[n] = is_pushed_list[i]

        self.storage.save_selection_results(
            expno=self.expno,
            number=self.card_selection.number, time=time_delta,
            positions=positions, status=status
        )

    def get_card_texts(self):
        return [card.text for card in self.shuffled_cards]

    def get_i1(self):
        return self.card_selection.instructions_p1

    def get_i2(self):
        return self.card_selection.instructions_p2

    def get_t1(self):
        return self.card_selection.text_p1

    def get_t2(self):
        return self.card_selection.text_p2

    def get_rule(self):
        return self.card_selection.rule


class DummyCardController(object):
    def get_card_texts(self):
        return ["" for i in range(4)]

    def get_i1(self):
        return ""

    def get_i2(self):
        return ""

    def get_t1(self):
        return ""

    def get_t2(self):
        return ""

    def get_rule(self):
        return ""

    def show_all_at_once(self):
        return True

    def start(self):
        pass

    def end(self, _):
        pass
