from time import time
from random import shuffle


class CardController(object):
    storage = None
    card_selection = None
    is_recording = None
    expno = None
    shuffled_cards = None
    card_permutation = None
    start_time = None

    def __init__(self, storage, card_selection, is_recording, expno):
        self.storage = storage
        self.card_selection = card_selection
        self.is_recording = is_recording
        self.expno = expno
        self.shuffled_cards = shuffle(self.card_selection.cards)
        self.card_permutation = [1, 2, 3, 4]
        for i in range(4):
            self.card_permutation[self.shuffled_cards[i].number] = i

    def show_all_at_once(self):
        return False

    def start(self):
        self.start_time = time()

    def end(self, is_pushed_list):
        pass

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
