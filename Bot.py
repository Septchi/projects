import threading
import time

from pynput.keyboard import Key, Listener, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController

from ImageProcessing import ImageProcessing
class Bot():

    def __init__(self):

        self.speed = 0.05
        self.botStart = False
        self.keyboard = keyboardController()
        self.mouse = mouseController()

        #self.botThread = threading.Thread(target=self.input)
    def onPress(self, key):
        try:
            if key.char == 'b':
                if self.botStart:
                    self.botStart = False
                else:
                    self.botStart = True
                print(self.botStart)
        except AttributeError:
            print(key)

    def onRelease(self, key):
        if key == Key.esc:
            # Stop listener
            return False

    def input(self, key):
        self.keyboard.press(key)
        time.sleep(self.speed)
        self.keyboard.release(key)


    def start(self):
        #self.botThread.start()
        with Listener(on_press=self.onPress, on_release=self.onRelease) as listener:
            print('Listener has started')
            time.sleep(0.2)
            listener.join()