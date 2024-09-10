from mainWindow import MainWindow
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

widow = MainWindow(app)
widow.show()

app.exec()