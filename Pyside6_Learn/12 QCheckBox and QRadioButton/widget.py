from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QRadioButton, QCheckBox, QSizePolicy, QHBoxLayout, QButtonGroup, \
    QGridLayout


class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QRadioButton & QCheckBox")

        checkbox_group = QGroupBox("CheckBox")
        checkbox_group.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.window_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        checkbox_group.setLayout(os_layout)

        #Exclusive Checkboxes

        drinks = QGroupBox("Exclusive CheckBox")
        drinks.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        beer = QCheckBox("Beer")
        beer.toggled.connect(self.checkbox_toggled)
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)

        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        answers = QGroupBox("Choose Answer")
        answers.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_a.setChecked(True)

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(answer_a)
        answer_layout.addWidget(answer_b)
        answer_layout.addWidget(answer_c)
        answers.setLayout(answer_layout)

        grid_layout = QGridLayout()
        grid_layout.addWidget(checkbox_group, 0, 0)
        grid_layout.addWidget(drinks, 0, 1)
        grid_layout.addWidget(answers, 1, 0, 1, 2)

        self.setLayout(grid_layout)
    def window_box_toggled(self, checked):
        if (checked):
            print("Window button checked")
        else:
            print("Window button unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("Linux button checked")
        else:
            print("Linux button unchecked")

    def mac_box_toggled(self, checked):
        if (checked):
            print("Mac button checked")
        else:
            print("Mac button unchecked")

    def checkbox_toggled(self, checked):
        if (checked):
            print(f"Beer Button Checked")
        else:
            print(f"Beer Button Unchecked")
