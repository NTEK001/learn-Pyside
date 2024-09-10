#VERSION1:
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First MainWindow App")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()
app.exec()
"""

#VERSION2:
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
"""
from PySide6.QtWidgets import QApplication
import sys
from button_holder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()