import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyNote'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(self.width, self.height)
    
        # Create textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,200)
        
        self.show()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())