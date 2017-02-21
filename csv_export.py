import sys
from exporter import Application
from common import Storage

if __name__ == '__main__':
    storage = Storage("db.json")
    app = Application(storage, sys.argv)
    sys.exit(app.run())
