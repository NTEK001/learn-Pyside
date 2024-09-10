from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel


class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LineEdit Widget")

        label = QLabel("User Name : ")
        self.line_edit = QLineEdit()
        #self.line_edit.textChanged.connect(self.text_changed)
        #self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        #self.line_edit.editingFinished.connect(self.edit_finished)
        #self.line_edit.selectionChanged.connect(self.selection_change)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab Data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I am here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def button_clicked(self):
        var = self.line_edit.displayText()
        #print(var)
        self.text_holder_label.setText(var)

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print(f"Old Cursor Position - {old} \nNew Cursor Position - {new}")

    def edit_finished(self) :
        print("Editing Finished")
        self.text_changed()

    def selection_change(self):
        print(f"Selection Change : {self.line_edit.selectedText()}")

    def text_edited(self,newText):
        print(f"New text is {newText}")
