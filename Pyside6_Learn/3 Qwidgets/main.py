from PySide6.QtWidgets import QApplication
import sys
from rockwidget import Rockwidget

app = QApplication()
window = Rockwidget()
window.show()

app.exec()