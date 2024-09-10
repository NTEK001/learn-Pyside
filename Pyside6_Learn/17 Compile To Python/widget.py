from PySide6.QtWidgets import  QWidget
from PySide6.QtCore import Qt
from ui_widget import Ui_Form

class widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.submit_button.clicked.connect(self.do_something)

    def do_something(self):
        print(f"{self.fullname_lineedit.text()} is a {self.occupation_lineedit.text()}")
