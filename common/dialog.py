from PyQt5.QtWidgets import QDialog


class UnrejectableDialog(QDialog):
    def reject(self):
        pass
