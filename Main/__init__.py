import sys
import pyautogui
import CommonUtils.obscure as obscure
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

    def yuhun(self):
        self.LogBrowser.append("御魂执行......")
        width, height = pyautogui.size()  # 屏幕的宽度和高度
        str1 = '屏幕分辨率:{} * {}'.format(width, height)
        self.LogBrowser.append(str1)

        file = open(scriptDir + scriptJsqDir)
        list = []
        while True:
            text = file.readline()  # 只读取一行内容
            # 判断是否读取到内容
            if not text:
                break
            self.LogBrowser.append(text.replace("\n", ""))
            list.append(text.replace("\n", ""))
        file.close()

        for k, v in enumerate(list):
            print(k, v)
            x = v.split(":")
            print(x[0], x[1])
            if x[0] == 'P':
                path = JsqDir + x[1]
                x1 = -1
                y1 = -1
                try:
                    self.LogBrowser.append("定位>>>>>>" + path)
                    x1, y1 = pyautogui.locateCenterOnScreen(path, grayscale=False,region=(1500, 0, 500, 700))
                # self.LogBrowser.append("定位坐标>>>>>>{},{}".format(x1, y1))
                except :
                    self.LogBrowser.append("find error")
                    print("find error")
                if x1 != -1 or y1 != -1:
                    pyautogui.moveTo(x1, y1)
                    pyautogui.click()
                    pyautogui.moveTo(0, 0)
            if x[0] == 'T':
                t1=x[1].split(",")
                obscure.sleepRandomTime(int(t1[0]),int(t1[1]))

    def juexing(self):
        self.LogBrowser.append("觉醒执行中......")


# app = QApplication(sys.argv)
# w = MainWindow()
# w.show()
# w.resize(800, 600)
# w.setWindowIcon(QIcon('..\\res\\img\\icon.jpg'))
# sys.exit(app.exec())

width, height = pyautogui.size()  # 屏幕的宽度和高度
str1 = '屏幕分辨率:{} * {}'.format(width, height)

file = open(scriptDir + scriptJsqDir)
list = []
while True:
    text = file.readline()  # 只读取一行内容
    # 判断是否读取到内容
    if not text:
        break
    list.append(text.replace("\n", ""))
file.close()

for k, v in enumerate(list):
    print(k, v)
    x = v.split(":")
    print(x[0], x[1])
    if x[0] == 'P':
        path = JsqDir + x[1]
        x1 = -1
        y1 = -1
        # try:
        x1, y1 = pyautogui.locateCenterOnScreen(path, grayscale=False, region=(1500, 0, 500, 700))
        # except:
        #     print("find error")
        print(x1, y1)
        if x1 != -1 or y1 != -1:
            pyautogui.moveTo(x1, y1)
            pyautogui.click()
            pyautogui.moveTo(0, 0)
    if x[0] == 'T':
        t1 = x[1].split(",")
        obscure.sleepRandomTime(int(t1[0]), int(t1[1]))
