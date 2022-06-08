from pynput.mouse import Listener as mouseListener, Button
from pynput.keyboard import Listener as keyListener
from keyboard import press, release
from random import randint as rand

from time import sleep
from threading import Thread
running = False
def on_press(key):
    global running
    try:
        if key.char == 'u':
            if not running:
                running = True
                print("running")
            elif running:
                running = False
                print('not running')
    except AttributeError:
        return 0


def main():
    while True:
        if running:
            press('w')
            sleep(1)
            release('w')
            press('a')
            sleep(1)
            release('a')
            press('s')
            sleep(1)
            release('s')
            press('d')
            sleep(1)
            release('d')
keyListener = keyListener(on_press=on_press)
mainThread = Thread(target=main)
mainThread.start()
keyListener.start()
keyListener.join()

