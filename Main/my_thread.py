from PyQt5.QtCore import *
import pyautogui
import CommonUtils.obscure as obscure

# 继承QThread

class RunThread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(str)

    def setDir(self,dir):
        self.dir = dir

    def __init__(self, MainWindow, parent=None):
        super().__init__(parent)
        self.MainWindow = MainWindow
        self.dir = None

    def run(self):
        self.script()

    def script(self):
        width, height = pyautogui.size()  # 屏幕的宽度和高度
        str1 = '屏幕分辨率:{} * {}'.format(width, height)
        self.breakSignal.emit(str1)

        file = open(self.dir)
        list = []
        re_time = 0
        while True:
            text = file.readline()  # 只读取一行内容
            # 判断是否读取到内容
            if not text:
                break
            self.breakSignal.emit(text.replace("\n", ""))
            list.append(text.replace("\n", ""))
        file.close()
        count = 0
        while re_time - count >= 0:
            for k, v in enumerate(list):
                print(k, v)
                x = v.split(":")
                print(x[0], x[1])
                if x[0] == 'P':
                    path = self.dir + x[1]
                    x1 = -1
                    y1 = -1
                    try:
                        self.breakSignal.emit("定位>>>>>>" + path)
                        x1, y1 = pyautogui.locateCenterOnScreen(path, grayscale=False, region=(1500, 0, 500, 700))
                        self.breakSignal.emit("定位坐标>>>>>>{},{}".format(x1, y1))
                    except:
                        self.breakSignal.emit("find error")
                        print("find error")
                    if x1 != -1 or y1 != -1:
                        pyautogui.moveTo(x1, y1)
                        pyautogui.click()
                        pyautogui.moveTo(0, 0)
                if x[0] == 'T':
                    t1 = x[1].split(",")
                    obscure.sleepRandomTime(int(t1[0]), int(t1[1]))
                if x[0] == 'R':
                    re_time = int(x[1])
            count = count + 1
