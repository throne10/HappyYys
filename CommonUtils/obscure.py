import os
import cv2
import random
import time

import pyautogui


def sleepRandomTime(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))


def getRandomPoint(p1, p2):
    """产生一个坐标在在p1,p2之间的二维区域内的随机位置"""
    if p1[0] <= p2[0]:
        xc = random.randint(p1[0], p2[0])
    else:
        xc = random.randint(p2[0], p1[0])
    if p1[1] <= p2[1]:
        yc = random.randint(p1[1], p2[1])
    else:
        yc = random.randint(p2[1], p1[1])
    return xc, yc
