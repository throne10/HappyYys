import CommonUtils.obscure as obscure
import pyautogui

# print(obscure.getRandomPoint((1, 1), (4, 4)))
# obscure.sleepRandomTime(1, 2)
# print(obscure.getRandomPoint((4, 4), (1, 1)))
x,y =pyautogui.locateCenterOnScreen('eq.png',grayscale=False,region=(1500, 0, 500, 700))
pyautogui.moveTo(x,y)

