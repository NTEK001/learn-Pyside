import sys
from PySide6 import QtWidgets
from widget import widget

app = QtWidgets.QApplication(sys.argv)
window = widget()
window.show()

app.exec()