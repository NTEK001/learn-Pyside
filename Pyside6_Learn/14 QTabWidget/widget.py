from PySide6.QtWidgets import QWidget, QHBoxLayout,QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget")

        tab_widget = QTabWidget(self)

        #Information
        widget_form = QWidget()
        label_full_name = QLabel("Full Name : ")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        #Buttons
        widget_button = QWidget()
        button_1 = QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 = QPushButton("Three")

        button_1.clicked.connect(self.button_clicked)
        button_2.clicked.connect(self.button_clicked)
        button_3.clicked.connect(self.button_clicked)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button_1)
        button_layout.addWidget(button_2)
        button_layout.addWidget(button_3)

        widget_button.setLayout(button_layout)

        tab_widget.addTab(widget_form,"Information")
        tab_widget.addTab(widget_button,"Button")

        layout = QHBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def button_clicked(self):
        print("Button Clicked")
