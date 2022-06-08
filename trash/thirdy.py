from pynput.keyboard import Key, Controller, Listener
import time
import threading


def function():
    keyboard = Controller()

    while True:
        if not paused:
            keyboard.type('@claus')
            keyboard.press(Key.tab)
            keyboard.press(Key.enter)
        time.sleep(1.5)


def on_press(key):
    global paused

    if paused:
        if "f3" in str(key):
            paused = False
    else:
        if "f4" in str(key):
            paused = True


# global variables with default values at star
paused = True

# run long-running `function` in separated thread
thread = threading.Thread(target=function)  # function's name without `()`
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()