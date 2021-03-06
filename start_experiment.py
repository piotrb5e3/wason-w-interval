import sys
from experiment_runner import Application, ExperimentController
from common import Config, Storage, CardSelection, Card

if __name__ == '__main__':
    storage = Storage("db.json")
    app = Application(storage, sys.argv)
    sys.exit(app.run())
