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
    experiment_config = None
    experiment_mode = None


    def __init__(self, experiment_config):
        self.experiment_config = experiment_config

    def set_mode(self, mode):
        self.experiment_mode = MODES[mode]

    def submit_user_data(self, name, sex, age):
        print('RCVD!')
