import sys

from config_maker import Application

if __name__ == '__main__':
    app = Application(sys.argv)
    sys.exit(app.run())
