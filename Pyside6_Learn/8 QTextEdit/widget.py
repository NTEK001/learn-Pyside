from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QTextEdit

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit Widget")

        self.text_edit = QTextEdit()

        current_text_button = QPushButton("Current Button")
        current_text_button.clicked.connect(self.current_text_button_clicked)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set Plain Text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set HTML")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)
        self.setLayout(v_layout)

    def current_text_button_clicked(self):
        print(self.text_edit.toPlainText())

    def set_plain_text(self):
        self.text_edit.setPlainText("Viva La Vila")

    def set_html(self):
        self.text_edit.setHtml('<h2>About Me</h2><p>Hello! I\'m [Your Name], and this is a simple webpage created with HTML and CSS. Here you can write a brief introduction about yourself or the purpose of the website.</p><h2>My Interests</h2><p>I enjoy coding, reading, and spending time outdoors. This section can include more details about your hobbies and interests.</p><h2>Contact</h2><p>You can reach me at <a href="mailto:your.email@example.com">your.email@example.com</a>.</p></div>')
