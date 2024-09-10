from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Rockwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")
        button1 = QPushButton("Button1")
        button1.clicked.connect(self.Button_clicked1)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.Button_clicked2)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def Button_clicked1(self):
        print('Button1 Clicked')

    def Button_clicked2(self):
        print('Button2 Clicked')
