import pyautogui


def locateOnScreen(imge):
    location = pyautogui.locateOnScreen(imge)
    print("locateOnScreen", location)
    if location != None:
        x, y = pyautogui.center(location)  # 转化为 x,y坐标
        print(x, y)  # 按键5的坐标是
        return x, y
    else:
        return None
