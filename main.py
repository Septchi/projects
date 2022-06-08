import cv2 as cv
import pyautogui

from pynput.keyboard import Key, Listener, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController

import numpy as np
import time
import threading
import win32gui, win32ui, win32con

from ImageProcessing import ImageProcessing
from Bot import Bot
#Initialized ImageProcessing Class
window = "SuperNova - https://chat.kongregate.com/gamez/0024/9627/live/game.swf?kongregate_game_version=1564415602"
hwnd = win32gui.FindWindow(None, window)
imgProc = ImageProcessing(hwnd)
bot = Bot(imgProc)

#Initialized variables
loopTime = time.time()
#crop hieght and width

#instatiate image thread
imgThread = threading.Thread(target=imgProc.processImage)

def main():
    #imgProc.listWindows()
    #Main Algorithm
    global loopTime
    imgThread.start()
    bot.start()




if __name__ == '__main__':
    main()

