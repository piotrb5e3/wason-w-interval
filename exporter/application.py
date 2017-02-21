from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QApplication, QMessageBox, QFileDialog)

from .export import export, ExportException

CSV_FILTER = "CSV file (*.csv)"


class Application(object):
    app = None
    storage = None
    args = None
    msg = None

    _startup_timer = None

    def __init__(self, storage, args):
        self.args = args
        self.storage = storage

    def run(self):
        self.app = QApplication(self.args)
        self._startup_timer = QTimer().singleShot(0, self.on_started)
        return self.app.exec_()

    def on_started(self):
        if not self.storage.has_complete_data():
            self.show_no_data_to_export_error()
        else:
            self.select_target_file()

    def show_no_data_to_export_error(self):
        self.msg = QMessageBox(None)
        self.msg.setText("Error!\nNo data to export!")
        self.msg.setFixedSize(200, 100)
        self.msg.show()

    def select_target_file(self):
        fname = QFileDialog.getSaveFileName(caption="Save as",
                                            filter=CSV_FILTER)

        fname = fname[0]

        if not fname:
            return

        if not fname.endswith(".csv"):
            fname += ".csv"
        try:
            export(filename=fname, storage=self.storage)
            self.msg = QMessageBox(None)
            self.msg.setText("Export finished successfully!")
            self.msg.show()
        except ExportException as e:
            self.msg = QMessageBox(None)
            self.msg.setText("An error occurred during export:")
            self.msg.setDetailedText(str(e))
            self.msg.show()
