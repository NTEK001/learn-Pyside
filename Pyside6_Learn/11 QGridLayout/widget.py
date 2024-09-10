from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton,  QSizePolicy

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout")

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        button6 = QPushButton("Six")
        button7 = QPushButton("Seven")

        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        grid_layout = QGridLayout()
        grid_layout.addWidget(button1, 0, 0)
        grid_layout.addWidget(button2, 0, 1, 1, 2)
        grid_layout.addWidget(button3, 1, 0, 2, 1)
        grid_layout.addWidget(button4, 1, 1)
        grid_layout.addWidget(button5, 1, 2)
        grid_layout.addWidget(button6, 2, 1)
        grid_layout.addWidget(button7, 2, 2)

        self.setLayout(grid_layout)


