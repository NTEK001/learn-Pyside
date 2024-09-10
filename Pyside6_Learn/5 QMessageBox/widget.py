from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QPushButton
from PySide6.QtGui import QIcon


class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        self.setLayout(layout)

    def button_clicked_hard(self):
        print("Hard")
        self.button_clicked_message("Hard Button Pressed")

    def button_clicked_critical(self):
        print("Critical")
        self.button_clicked_message("Critical Button Pressed")

    def button_clicked_question(self):
        print("Question")
        self.button_clicked_message("Question Button Pressed")

    def button_clicked_information(self):
        print("Information")
        self.button_clicked_message("Information Button Pressed")

    def button_clicked_warning(self):
        print("Warning")
        self.button_clicked_message("Warning Button Pressed")

    def button_clicked_message(self,messageText):

        message = QMessageBox()
        message.setMinimumSize(300, 300)
        message.setWindowTitle("Message Box")
        message.setText(messageText)
        message.setInformativeText("What do you want to do?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("User Choose OK")
        else:
            print("User Choose Cancel")