from common import (Config, load_config, ConfigException, CardSelection,
                    save_config)
from .card_selection_conf_controller import CardSelectionConfigController


class ConfigController(object):
    conf = None

    def __init__(self):
        self.cs_controllers = []

    def new_conf(self):
        self.conf = Config()

    def conf_with_filename(self, filename):
        try:
            self.conf = load_config(filename)
            return True
        except ConfigException:
            return False

    def get_edit_cs_controller(self, n):
        return CardSelectionConfigController(self.conf.card_selections[n], self,
                                             pos=n)

    def get_add_cs_controller(self):
        cs = CardSelection()
        return CardSelectionConfigController(cs, self)

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
            save_config(filename, self.conf)
            return True
        except ConfigException:
            return False

    def get_cs_controllers(self):
        return [CardSelectionConfigController(cs, self) for cs in
                self.conf.card_selections]

    def add_cs(self, cs):
        self.conf.card_selections.append(cs)

    def update_cs(self, cs, pos):
        self.conf.card_selections[pos] = cs

    def delete_nth_cs(self, n):
        del self.conf.card_selections[n]

    def move_up(self, n):
        if n > 0:
            tmp = self.conf.card_selections[n - 1]
            self.conf.card_selections[n - 1] = self.conf.card_selections[n]
            self.conf.card_selections[n] = tmp

    def move_down(self, n):
        if n < len(self.conf.card_selections) - 1:
            tmp = self.conf.card_selections[n + 1]
            self.conf.card_selections[n + 1] = self.conf.card_selections[n]
            self.conf.card_selections[n] = tmp


class ControllerException(BaseException):
    pass
