import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTextBrowser
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('..\\untitled.ui', self)
        self.YuHunButton.clicked.connect(self.yuhun)
        self.JueXingButton.clicked.connect(self.juexing)

    def yuhun(self):
        self.LogBrowser.append("御魂执行中......")
    def juexing(self):
        self.LogBrowser.append("觉醒执行中......")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
w.resize(800, 600)
sys.exit(app.exec())
