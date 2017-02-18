import sys
from experiment_runner import Application, ExperimentController
from common import Config, Storage, CardSelection, Card


def test_conf():
    c = Config()
    c.experiment_name = "Rando"
    c.ig_training_session_time = 2
    c.ig_measuring_session_time = 2
    c.ig_w_selection_training_session_time = 2
    c.ig_no_clicking_warning_time = 3
    c.ig_instructions_text = "Klikaj"
    c.ig_pre_measuring_session_text = "Klikaj - patrzymy!"
    c.ig_w_selection_instructions_text = "Klikaj i klikaj"
    c.thanks_text = "Dzięki"
    c.card_selections = []

    cs = CardSelection()
    cs.number = 0
    cs.is_fixed_position = True
    cs.text_p1 = "This is a fixed position card selection"
    cs.rule = "XXX"
    cs.text_p2 = "More Text!"
    cs.instructions_p1 = "Inp1"
    cs.instructions_p2 = "Inp2"
    cs.cards = []
    crd = Card()
    crd.number = 1
    crd.text = "C1"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 2
    crd.text = "C2"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 3
    crd.text = "C3"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 4
    crd.text = "C4"
    cs.cards.append(crd)
    c.card_selections.append(cs)

    cs = CardSelection()
    cs.number = 0
    cs.is_fixed_position = False
    cs.text_p1 = "This is the first random card selection"
    cs.rule = "XXX"
    cs.text_p2 = "More Text!"
    cs.instructions_p1 = "Inp1"
    cs.instructions_p2 = "Inp2"
    cs.cards = []
    crd = Card()
    crd.number = 1
    crd.text = "C1_"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 2
    crd.text = "C2_"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 3
    crd.text = "C3_"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 4
    crd.text = "C4_"
    cs.cards.append(crd)
    c.card_selections.append(cs)

    cs = CardSelection()
    cs.number = 0
    cs.is_fixed_position = True
    cs.text_p1 = "This is the second random card selection"
    cs.rule = "An actual rule!"
    cs.text_p2 = "More Text!"
    cs.instructions_p1 = "Inp1 LOL"
    cs.instructions_p2 = "Inp2"
    cs.cards = []
    crd = Card()
    crd.number = 1
    crd.text = "C101"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 2
    crd.text = "C201"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 3
    crd.text = "C301"
    cs.cards.append(crd)
    crd = Card()
    crd.number = 4
    crd.text = "C401"
    cs.cards.append(crd)
    c.card_selections.append(cs)
    return c


if __name__ == '__main__':
    conf = test_conf()
    storage = Storage("db.json")
    controller = ExperimentController(conf, storage)
    app = Application(controller, sys.argv)
    sys.exit(app.run())
