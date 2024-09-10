from PySide6.QtWidgets import QApplication
import sys
from widget import widget

app = QApplication(sys.argv)
window = widget()
window.show()

app.exec()


# import sys
# import os
# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtWebEngineWidgets import QWebEngineView
# from PySide6.QtCore import QUrl

# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.browser = QWebEngineView()
#         self.setCentralWidget(self.browser)

#         # Load a local HTML file
#         local_file = os.path.abspath("/Users/yasharya/Documents/projects/PySide6/venv/Pyside6_Learn/QWebEngine/web_map.html")
#         self.browser.setUrl(QUrl.fromLocalFile(local_file))

#         self.setWindowTitle("PySide6 Browser")
#         self.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Browser()
#     sys.exit(app.exec())

# import sys
# import os
# from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
# from PySide6.QtWebEngineWidgets import QWebEngineView
# from PySide6.QtCore import QUrl
#
#
# class MyWebEngineView(QWebEngineView):
#     def createWindow(self, _type):
#         new_view = MyWebEngineView()
#         new_view.show()
#         return new_view
#
#
# class Browser(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.browser = MyWebEngineView()
#         self.setCentralWidget(self.browser)
#         # local_file = os.path.abspath(
#         #     "/Users/yasharya/Documents/projects/PySide6/venv/Pyside6_Learn/QWebEngine/map.html")
#         self.browser.setUrl(QUrl("http://localhost:8000/map.html"))
#
#         self.setWindowTitle("PySide6 Browser")
#         self.show()
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Browser()
#     sys.exit(app.exec())
