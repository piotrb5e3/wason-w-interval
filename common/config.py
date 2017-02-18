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
