from pickle import dump, load


def load_config(filename):
    try:
        f = open(filename, mode='rb')
        conf = load(f)
        f.close()
        return conf
    except OSError:
        raise ConfigException


def save_config(filename, conf):
    try:
        f = open(filename, mode='wb')
        dump(conf, f)
        f.close()
    except OSError:
        raise ConfigException


class Config(object):
    # Time in seconds
    ig_training_session_time = ''
    ig_measuring_session_time = ''
    ig_w_selection_training_session_time = ''
    ig_no_clicking_warning_time = ''

    # Texts
    welcome_text = ''
    ig_instructions_text = ''
    ig_pre_measuring_session_text = ''
    ig_w_selection_instructions_text = ''
    pre_experiment_text = ''
    thanks_text = ''
    cs_instructions_short = ''

    card_selections = None

    def __init__(self):
        self.card_selections = []


class CardSelection(object):
    number = None
    is_fixed_position = None
    text_p1 = None
    rule = None
    text_p2 = None
    instructions = None
    cards = None

    def __init__(self):
        self.cards = [Card(n) for n in range(1, 5)]


class Card(object):
    number = None
    text = None

    def __init__(self, no):
        self.number = no
        self.text = ""


class ConfigException(BaseException):
    pass
