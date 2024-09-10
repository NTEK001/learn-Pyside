from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import os

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QWebEngine")

        self.view = QWebEngineView()
        local_file = "https://www.youtube.com/watch?v=c1wkx1V1qHY"
        self.view.setUrl(QUrl(local_file))
        layout = QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

