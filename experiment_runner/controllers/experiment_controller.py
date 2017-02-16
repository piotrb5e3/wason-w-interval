from .click_controller import ClickController
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

    def __init__(self, experiment_config, storage):
        self.experiment_config = experiment_config
        self.storage = storage
        self.exp_ptr = 0

    def has_data(self):
        return self.storage.has_data()

    def purge_data(self):
        self.storage.purge()

    def set_mode(self, mode):
        if mode not in MODES:
            raise ValueError("Incorrect Mode")
        self.experiment_mode = mode

    def submit_user_data(self, name, sex, age):
        self.storage.save_user_info(name=name, sex=sex, age=age)

    def get_click_training_controller(self):
        nc_timeout = self.experiment_config.ig_no_clicking_warning_time
        return ClickController(storage=self.storage, is_recording=False,
                               mode=self.experiment_mode, expno=0,
                               no_clicking_timeout=nc_timeout)

    def get_click_measuring_controller(self):
        nc_timeout = self.experiment_config.ig_no_clicking_warning_time
        return ClickController(storage=self.storage, is_recording=True,
                               mode=self.experiment_mode, expno=0,
                               no_clicking_timeout=nc_timeout)

    def get_next_click_card_controllers(self):
        if self.exp_ptr >= len(self.experiment_config.card_selections):
            raise Exception("No more experiments")

        cardc = CardController(self.storage,
                               self.experiment_config.card_selections[
                                   self.exp_ptr],
                               True,
                               self.exp_ptr + 1)

        clickc = ClickController(self.storage,
                                 True,
                                 self.experiment_mode,
                                 self.exp_ptr + 1,
                                 self.experiment_config.ig_no_clicking_warning_time)
        self.exp_ptr += 1
        return clickc, cardc

    def has_more_experiments(self):
        return self.exp_ptr < len(self.experiment_config.card_selections)

    def get_click_training_time(self):
        return self.experiment_config.ig_training_session_time

    def get_click_measuring_time(self):
        return self.experiment_config.ig_measuring_session_time

    def get_thank_you_text(self):
        return self.experiment_config.thanks_text

    def get_interval_instructions_text(self):
        return self.experiment_config.ig_instructions_text

    def get_interval_pre_measurement_text(self):
        return self.experiment_config.ig_pre_measuring_session_text

    def get_selection_instructions_text(self):
        return self.experiment_config.ig_w_selection_instructions_text
