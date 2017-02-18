from pickle import dump, load

from config import Config


class ConfigController(object):
    conf = None
    cs_controllers = None

    def __init__(self):
        self.cs_controllers = []

    def new_conf(self):
        self.conf = Config()

    def conf_with_filename(self, filename):
        try:
            f = open(filename, mode='rb')
            self.conf = load(f)
            f.close()
            return True
        except OSError as e:
            print('Exception: ' + str(e))
            return False

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
            self.conf.ig_measuring_session_time = int(time_str)
        except ValueError:
            pass

    def set_no_clicking_warning_time(self, time_str):
        try:
            self.conf.ig_no_clicking_warning_time = int(time_str)
        except ValueError:
            pass

    def get_ig_instr(self):
        return self.conf.ig_instructions_text

    def get_ig_measuring_instr(self):
        return self.conf.ig_pre_measuring_session_text

    def get_ig_w_cs_training_instr(self):
        return self.conf.ig_w_selection_instructions_text

    def get_pre_exp_instr(self):
        return self.conf.pre_experiment_text

    def get_pre_exp_w_click_instr(self):
        return self.conf.pre_experiment_w_click_text

    def get_thanks_text(self):
        return self.conf.thanks_text

    def set_ig_instr(self, txt):
        self.conf.ig_instructions_text = txt

    def set_ig_measuring_instr(self, txt):
        self.conf.ig_pre_measuring_session_text = txt

    def set_ig_w_cs_training_instr(self, txt):
        self.conf.ig_w_selection_instructions_text = txt

    def set_pre_exp_instr(self, txt):
        self.conf.pre_experiment_text = txt

    def set_pre_exp_w_click_instr(self, txt):
        self.conf.pre_experiment_w_click_text = txt

    def set_thanks_text(self, txt):
        self.conf.thanks_text = txt

    def get_errors_list(self):
        return []

    def save(self, filename):
        try:
            f = open(filename, mode='wb')
            dump(self.conf, f)
            f.close()
            return True
        except OSError as e:
            print('Exception: ' + str(e))
            return False


class CardSelectionConfigController(object):
    cs = None

    def __init__(self, cs):
        self.cs = cs


class ControllerException(BaseException):
    pass
