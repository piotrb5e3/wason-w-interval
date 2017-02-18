class Config(object):
    experiment_name = None

    # Time in seconds
    ig_training_session_time = None
    ig_measuring_session_time = None
    ig_w_selection_training_session_time = None
    ig_no_clicking_warning_time = None

    # Texts
    ig_instructions_text = None
    ig_pre_measuring_session_text = None
    ig_w_selection_instructions_text = None
    thanks_text = None

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
