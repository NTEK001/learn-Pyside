from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_widget import Ui_Widget
import resource_rc

class widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("Plus and Minus")
        self.spin_box.setValue(50)
        self.plus_button.clicked.connect(self.plus)
        self.minus_button.clicked.connect(self.minus)

        plus_icon = QIcon(":/plus-sign-vector-icon-3637140246.jpg")
        minus_button = QIcon(":/minus-vector-icon-330659772.jpg")

        self.plus_button.setIcon(plus_icon)
        self.minus_button.setIcon(minus_button)

    def plus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value+1)

    def minus(self):
        value = self.spin_box.value()
        self.spin_box.setValue(value-1)