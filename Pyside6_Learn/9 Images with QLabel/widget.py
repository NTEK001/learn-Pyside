from PySide6.QtWidgets import QWidget, QLabel,QHBoxLayout, QPushButton
from PySide6.QtGui import QPixmap

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("")
        image_label_1 = QLabel()
        image_label_1.setPixmap(QPixmap(""))

        layout = QHBoxLayout()
        layout.addWidget(image_label_1)
        self.setLayout(layout)