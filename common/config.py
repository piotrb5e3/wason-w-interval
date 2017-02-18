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
    experiment_name = None

    # Time in seconds
    ig_training_session_time = ''
    ig_measuring_session_time = ''
    ig_w_selection_training_session_time = ''
    ig_no_clicking_warning_time = ''

    # Texts
    ig_instructions_text = ''
    ig_pre_measuring_session_text = ''
    ig_w_selection_instructions_text = ''
    pre_experiment_text = ''
    pre_experiment_w_click_text = ''
    thanks_text = ''

    card_selections = None


class CardSelection(object):
    number = None
    is_fixed_position = None
    text_p1 = None
    rule = None
    text_p2 = None
    instructions_p1 = None
    instructions_p2 = None
    cards = None


class Card(object):
    number = None
    text = None


class ConfigException(BaseException):
    pass
