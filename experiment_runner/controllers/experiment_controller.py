from random import shuffle

from .click_controller import ClickController, DummyClickController
from .card_controller import CardController

MODES = [
    'NO_FEEDBACK_EXPERIMENT',
    'FEEDBACK_EXPERIMENT',
    'CONTROL_GROUP',
    'PILOT'
]


class ExperimentController(object):
    storage = None
    experiment_config = None
    experiment_mode = None
    session_start_time = None
    exp_ptr = None
    shuffled_card_selections = None

    def __init__(self, experiment_config, storage):
        self.experiment_config = experiment_config
        self.storage = storage
        self.exp_ptr = 0
        self.order_card_selections()

    def order_card_selections(self):
        self.shuffled_card_selections = []
        to_shuffle = []
        for cs in self.experiment_config.card_selections:
            if cs.is_fixed_position:
                self.shuffled_card_selections.append(cs)
            else:
                to_shuffle.append(cs)

        shuffle(to_shuffle)
        for cs in to_shuffle:
            self.shuffled_card_selections.append(cs)

    def set_mode(self, mode):
        if mode not in MODES:
            raise ValueError("Incorrect Mode")
        self.experiment_mode = mode

    def save_config_and_mode(self):
        self.storage.save_experiment_config(self.experiment_config,
                                            self.experiment_mode)

    def get_mode(self):
        return self.experiment_mode

    def is_pilot_mode(self):
        return self.experiment_mode == 'PILOT'

    def finish_experiment(self):
        self.save_config_and_mode()
        self.storage.save_completed_experiment()

    def submit_user_data(self, name, sex, age):
        self.storage.save_user_info(name=name, sex=sex, age=age)

    def get_click_training_controller(self):
        nc_timeout = self.experiment_config.ig_no_clicking_warning_time
        return ClickController(storage=self.storage, is_recording=False,
                               mode='FEEDBACK_EXPERIMENT', expno=0,
                               no_clicking_timeout=nc_timeout)

    def get_click_measuring_controller(self):
        nc_timeout = self.experiment_config.ig_no_clicking_warning_time
        return ClickController(storage=self.storage, is_recording=True,
                               mode=self.experiment_mode, expno=0,
                               no_clicking_timeout=nc_timeout)

    def get_next_click_card_controllers(self):
        if self.exp_ptr >= len(self.shuffled_card_selections):
            raise Exception("No more experiments")

        cardc = CardController(
            storage=self.storage,
            card_selection=self.shuffled_card_selections[self.exp_ptr],
            expno=self.exp_ptr + 1,
            controller=self)

        if self.experiment_mode in ('CONTROL_GROUP', 'PILOT'):
            clickc = DummyClickController()
        else:
            clickc = ClickController(
                storage=self.storage,
                is_recording=True,
                mode=self.experiment_mode,
                expno=self.exp_ptr + 1,
                no_clicking_timeout=self.experiment_config.ig_no_clicking_warning_time)

        self.exp_ptr += 1
        return clickc, cardc

    def has_more_experiments(self):
        return self.exp_ptr < len(self.experiment_config.card_selections)

    def get_welcome_text(self):
        return self.experiment_config.welcome_text

    def get_click_training_time(self):
        return self.experiment_config.ig_training_session_time

    def get_click_measuring_time(self):
        return self.experiment_config.ig_measuring_session_time

    def get_selection_training_time(self):
        return self.experiment_config.ig_w_selection_training_session_time

    def get_thank_you_text(self):
        return self.experiment_config.thanks_text

    def get_interval_instructions_text(self):
        return self.experiment_config.ig_instructions_text

    def get_interval_pre_measurement_text(self):
        return self.experiment_config.ig_pre_measuring_session_text

    def get_selection_training_instructions_text(self):
        return self.experiment_config.ig_w_selection_instructions_text

    def get_main_experiment_instructions_text(self):
        return self.experiment_config.pre_experiment_text

    def get_short_selection_instructions(self):
        return self.experiment_config.cs_instructions_short
