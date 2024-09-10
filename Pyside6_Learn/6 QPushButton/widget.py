from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QPushButton")

        button1 = QPushButton("Push Me")
        button1.clicked.connect(self.button_clicked)
        button1.pressed.connect(self.button_pressed)
        button1.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button1)
        self.setLayout(layout)

    def button_pressed(self):
        print("Button is Pressed")

    def button_released(self):
        print("Button is Released")

    def button_clicked(self):
        print("Button is Clicked")