from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()

        self.ui = loader.load("widget.ui", None)
        self.ui.setWindowTitle("User Data")
        self.ui.submit_button.clicked.connect(self.do_something)
    def show(self):
        self.ui.show()

    def do_something(self):
        print(f"{self.ui.fullname_lineedit.text()} is a {self.ui.occupation_lineedit.text()}")