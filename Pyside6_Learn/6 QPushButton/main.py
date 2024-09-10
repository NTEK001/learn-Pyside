from PySide6.QtWidgets import QApplication
from widget import widget
import sys

app = QApplication()

window = widget()
window.show()

app.exec()