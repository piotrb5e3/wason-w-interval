import sys
from experiment_runner import Application, Controller
from common import Config, Storage


def test_conf():
    c = Config()
    c.experiment_name = "Rando"
    c.ig_training_session_time = 20
    c.ig_measuring_session_time = 20
    c.ig_w_selection_training_session_time = 20
    c.ig_no_clicking_warning_time = 5
    c.ig_instructions_text = "Klikaj"
    c.ig_pre_measuring_session_text = "Klikaj - patrzymy!"
    c.ig_w_selection_instructions_text = "Klikaj i klikaj"
    c.thanks_text = "Dzięki"
    return c


if __name__ == '__main__':
    conf = test_conf()
    storage = Storage("db.json")
    controller = Controller(conf, storage)
    app = Application(controller, sys.argv)
    sys.exit(app.run())
