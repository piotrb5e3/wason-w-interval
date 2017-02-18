from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QFileDialog

from controller import ControllerException


class NewOrLoad(QDialog):
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        new_conf = QPushButton('New config')
        new_conf.clicked.connect(self.on_new_conf)
        from_file = QPushButton('From file')
        from_file.clicked.connect(self.on_from_file)

        vbox = QVBoxLayout()
        vbox.addWidget(new_conf)
        vbox.addWidget(from_file)
        self.setLayout(vbox)
        self.setGeometry(500, 300, 200, 100)
        self.show()

    def on_new_conf(self):
        self.controller.new_conf()
        self.accept()

    def on_from_file(self):
        fname = QFileDialog.getOpenFileName(
            self,
            'Open file',
            filter='Experiment Configuration (*.conf)')
        if not fname[0]:
            self.reject()
            return
        fname = fname[0]
        if self.controller.conf_with_filename(fname):
            self.accept()
        else:
            self.reject()
