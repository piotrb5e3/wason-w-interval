class CardSelectionConfigController(object):
    cs = None
    controller = None
    pos = None

    def __init__(self, cs, controller, pos=-1):
        self.cs = cs
        self.controller = controller
        self.pos = pos

    def save(self):
        if self.pos < 0:
            self.controller.add_cs(self.cs)
        else:
            self.controller.update_cs(self.cs, self.pos)

    def get_nth_card_text(self, n):
        return self.cs.cards[n].text

    def set_nth_card_text(self, n, text):
        self.cs.cards[n].text = text

    def get_task_text(self):
        return self.cs.text_p1

    def set_task_text(self, txt):
        self.cs.text_p1 = txt

    def get_rule(self):
        return self.cs.rule

    def set_rule(self, txt):
        self.cs.rule = txt

    def get_extra_text(self):
        return self.cs.text_p2

    def set_extra_text(self, txt):
        self.cs.text_p2 = txt

    def get_instructions(self):
        return self.cs.instructions

    def set_instructions(self, txt):
        self.cs.instructions = txt

    def is_fixed_position(self):
        return self.cs.is_fixed_position

    def set_is_fixed_position(self, val):
        self.cs.is_fixed_position = val
