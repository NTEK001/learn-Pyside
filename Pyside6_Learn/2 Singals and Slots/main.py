#Version1:
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
def button_clicked():
    print("The Button is Clicked")


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First MainWindow App")

button = QPushButton()
button.setText("Press Me")
button.released.connect(button_clicked)

window.setCentralWidget(button)

window.show()
app.exec()
"""

#Version2:
"""
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow


def button_clicked(data):
    print(f"The button is clicked and its state is: {data}")


app = QApplication()

window = QMainWindow()
window.setWindowTitle("Signals and Slots")

button = QPushButton("Click Me!")
button.setCheckable(True)
button.clicked.connect(button_clicked)

window.setCentralWidget(button)

window.show()
app.exec()
"""

#Version3:
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider, QMainWindow

def respond_to_slider(data):
    print(f"Slider moved to : {data}")

app = QApplication()
window = QMainWindow()
window.setWindowTitle("Slider Widget")

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)

window.setCentralWidget(slider)
window.show()

app.exec()
