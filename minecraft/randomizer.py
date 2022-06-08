from pynput.mouse import Listener as mouseListener, Button
from pynput.keyboard import Listener as keyListener
import keyboard
from random import randint as rand
running = False
def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.right and running:
            num = rand(1, maxW)
            #print(num)
            for i, w in enumerate(wList):
                if(num<=w):
                    keyboard.press_and_release(kList[i])
                    #print(f'{kList[i]} key has been pressed')
                    break

def on_press(key):
    global running
    try:
        if key.char == 'r':
            if not running:
                running = True
                print("running")
            elif running:
                running = False
                print('not running')
    except AttributeError:
        return 0
# Collect events until released
wList = []
kList = []

prevW=0
items = int(input("Input amount of items being randomized: "))
for i in range(items):
    wList.append(int(input(f'wieght of item {i+1}: ')) + prevW)
    prevW = wList[i]
maxW = wList[-1]
for i in range(items):
    kList.append(str(input(f'key of item {i + 1}: ')))
print(f'max weight is {maxW}')
print(f'weight List: {wList}')
mouseListener = mouseListener(on_click=on_click)
keyListener = keyListener(on_press=on_press)
mouseListener.start()
keyListener.start()
mouseListener.join()
keyListener.join()