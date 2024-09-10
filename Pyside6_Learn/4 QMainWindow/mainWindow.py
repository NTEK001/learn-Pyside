from __future__ import unicode_literals
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QStatusBar


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("custom MainWindow")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        quit_action = file_menu.addAction("Ext App")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        toolbar = QToolBar("My Main ToolBar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("Something")
        action1.triggered.connect(self.toolbar_button_action)
        toolbar.addAction(action1)

        img = QIcon("girl.png")
        toolbar.addSeparator()

        action2 = QAction(img, "Girl Button", self)
        action2.setStatusTip("This is the Girl Button")
        action2.setCheckable(True)
        action2.setChecked(False)
        action2.triggered.connect(self.toolbar_button_action)
        toolbar.addAction(action2)

        self.setStatusBar(QStatusBar(self))

    def quit_app(self):
        self.app.quit()

    def toolbar_button_action(self, data):
        self.statusBar().showMessage(f"Action 1 is Triggered status is {data}",300)
