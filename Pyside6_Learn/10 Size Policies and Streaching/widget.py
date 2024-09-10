from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size Policy and Stretches")

        label = QLabel("Some text : ")
        line_edit = QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")


        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button1,2)
        h_layout_2.addWidget(button2,1)
        h_layout_2.addWidget(button3,1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        self.setLayout(v_layout)