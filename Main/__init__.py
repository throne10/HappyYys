import sys
import pyautogui
import Main.my_thread
from Main.my_thread import RunThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon

scriptDir = '..\\res\\script\\'
scriptYuHunDir = 'yuhun\\yuhun.txt'
scriptJsqDir = 'jsq\\jsq.txt'
JsqDir = scriptDir + 'jsq\\'
# pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = False


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('..\\untitled.ui', self)
        self.YuHunButton.clicked.connect(self.yuhun)
        self.JueXingButton.clicked.connect(self.juexing)
    def log(self,text):
        self.LogBrowser.append(text)
    def yuhun(self):
        self.LogBrowser.append("御魂执行......")
        dir=scriptDir + scriptJsqDir
        thread.setDir(dir)
        thread.start()



    def juexing(self):
        self.LogBrowser.append("觉醒执行中......")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
w.resize(800, 600)
w.setWindowIcon(QIcon('..\\res\\img\\icon.jpg'))
thread=RunThread(w)
thread.breakSignal.connect(w.log)
sys.exit(app.exec())

