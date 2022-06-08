import cv2 as cv

import pyautogui

from pynput.keyboard import Key, Listener, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController

import numpy as np
import time
import threading

from ImageProcessing import ImageProcessing

#Initialized variables
botStart = False
clickStart = False
loopTime = 0

keyboard = keyboardController()
mouse = mouseController()

apple_img = cv.imread('../apple.jpeg', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(apple_img, apple_img, cv.TM_SQDIFF_NORMED)

def Screen():
    while (True):
        global loopTime
        screenshot = pyautogui.screenshot()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        print("FPS: {}".format(1 / (time.time() - loopTime)))
        loopTime = time.time()
        cv.imshow("Word", screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
    print("Done!")

def autoClicker():
    print('Clicker has Started')
    time.sleep(0.5)
    while True:
        if clickStart:
            print('button pressed')
            time.sleep(0.02)
            mouse.press(Button.left)
            mouse.release(Button.left)




def Bot():
    print('Bot has Started')
    while True:
        if botStart:
            keyboard.press('w')
            time.sleep(0.2)
            keyboard.release('w')
            keyboard.press('d')
            time.sleep(0.2)
            keyboard.release('d')
            keyboard.press('s')
            time.sleep(0.2)
            keyboard.release('w')
            print('nicu')

def on_press(key):
    try:
        if key.char == 'a':
            global botStart
            global clickStart
            print(clickStart)
            if clickStart:
                clickStart = False
            else:
                clickStart = True
    except AttributeError:
        print(key)

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False




#Intialize Threads
botThread = threading.Thread(target=autoClicker)


def main():
    #Main Algorithm
    #Screen()
    botThread.start()
    with Listener(on_press=on_press, on_release=on_release) as listener:
        print('Listener has started')
        listener.join()

if __name__ == '__main__':
    main()
