from config import Config


class ConfigController(object):
    conf = None
    cs_controllers = None

    def __init__(self):
        self.cs_controllers = []

    def new_conf(self):
        self.conf = Config()

    def conf_with_filename(self, filename):
        raise Exception("Not implemented")

    def get_training_session_time(self):
        return self.conf.ig_training_session_time

    def get_selection_training_session_time(self):
        return self.conf.ig_w_selection_training_session_time

    def get_measuring_session_time(self):
        return self.conf.ig_measuring_session_time

    def get_no_clicking_warning_time(self):
        return self.conf.ig_no_clicking_warning_time

    def set_training_session_time(self, time_str):
        try:
            self.conf.ig_training_session_time = int(time_str)
        except ValueError:
            pass

    def set_selection_training_session_time(self, time_str):
        try:
            self.conf.ig_w_selection_training_session_time = int(time_str)
        except ValueError:
            pass

    def set_measuring_session_time(self, time_str):
        try:
            self.conf.iig_measuring_session_time = int(time_str)
        except ValueError:
            pass

    def set_no_clicking_warning_time(self, time_str):
        try:
            self.conf.ig_no_clicking_warning_time = int(time_str)
        except ValueError:
            pass


class CardSelectionConfigController(object):
    cs = None

    def __init__(self, cs):
        self.cs = cs


class ControllerException(BaseException):
    pass
