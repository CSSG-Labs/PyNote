import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QMenuBar, QMenu
from PySide6.QtGui import QAction


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyNote'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()
        self. _createActions()
        self. _createMenuBar()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(self.width, self.height)

        # Create textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 200)

        self.show()

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        fileMenu = QMenu("&File", self)
        self.setMenuBar(menuBar)
        menuBar.addMenu(fileMenu)
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)

    def _createActions(self):

        # actions for new, open, save in menu
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        self.openAction = QAction("&Open", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
