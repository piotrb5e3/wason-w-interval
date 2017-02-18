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


class CardSelectionConfigController(object):
    cs = None

    def __init__(self, cs):
        self.cs = cs


class ControllerException(BaseException):
    pass
