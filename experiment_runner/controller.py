MODES = {
    'NO_FEEDBACK_EXPERIMENT': 1,
    'FEEDBACK_EXPERIMENT': 2,
    'CONTROL_GROUP': 3,
    'PILOT': 4
}

REV_MODES = {
    1: 'NO_FEEDBACK_EXPERIMENT',
    2: 'FEEDBACK_EXPERIMENT',
    3: 'CONTROL_GROUP',
    4: 'PILOT'
}


class Controller(object):
    storage = None
    experiment_config = None
    experiment_mode = None

    def __init__(self, experiment_config, storage):
        self.experiment_config = experiment_config
        self.storage = storage

    def has_data(self):
        return self.storage.has_data()

    def purge_data(self):
        self.storage.purge()

    def set_mode(self, mode):
        self.experiment_mode = MODES[mode]

    def submit_user_data(self, name, sex, age):
        self.storage.save_user_info(name=name, sex=sex, age=age)

    def is_not_clicking(self):
        return self.experiment_mode == MODES['NO_FEEDBACK_EXPERIMENT']

    def is_clicking_rhytmicly(self):
        return self.experiment_mode == MODES['FEEDBACK_EXPERIMENT']
