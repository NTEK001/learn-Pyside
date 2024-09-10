import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui",None)

def do_something(self):
    print(f'{window.fullname_lineedit.text()} is a {window.occupation_lineedit.text()}')

window.setWindowTitle("User Data")

window.submit_button.clicked.connect(do_something)
window.show()
app.exec()