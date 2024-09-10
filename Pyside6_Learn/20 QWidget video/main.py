import sys

from PySide6.QtWidgets import QWidget, QLabel, QApplication, QVBoxLayout
from PySide6.QtGui import QMovie
import PySide6.QtMultimedia

class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QMovie')
        self.setGeometry(500, 300, 300, 300)
        label = QLabel()
        movie = QMovie('/Users/yasharya/Downloads/Clouds free stock footage.mp4')
        movie.start()
        print(movie.isValid())
        label.setMovie(movie)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = widget()
    widget.show()
    sys.exit(app.exec())