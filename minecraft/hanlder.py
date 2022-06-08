from tkinter import *

from random import randint as rand

from pynput.mouse import Listener as mouseListener, Button as Butt
from keyboard import press_and_release
wList = []
kList = []

randomizeFlag = False
mainThreadFlag = True

window = Tk()
window.title('Block Randomizer')


def onClick(clickx, clicky, button, pressed):
    if pressed:
        if button == Butt.right and randomizeFlag:
            maxW = wList[-1]
            num = rand(1, maxW)
            # print(num)
            for i, w in enumerate(wList):
                if num <= w:
                    press_and_release(kList[i])
                    # print(f'{kList[i]} key has been pressed')
                    break

# def main():
#     global randomizeFlag
#     print('mainThread started')
#     while mainThreadFlag:
#         if randomizeFlag:
#             print('running')
#             sleep(0.5)
#     print('mainThread stopped')


def setWeight():
    global wList
    try:
        prevW = (wList[-1] if len(wList) > 0 else 0)
        wList.append(int(weightInput.get()) + prevW)
    except ValueError:
        return 0

    weightListLab['text'] = f'WeightList:{wList}'


def popWeight():
    global wList
    try:
        wList.pop(-1)
    except IndexError:
        return 0
    weightListLab['text'] = f'WeightList:{wList}'


def setKey():
    global kList
    kList.append(keyInput.get())
    keyListLab['text'] = f'KeyList:{kList}'


def popKey():
    global kList
    try:
        kList.pop(-1)
    except IndexError:
        return 0
    keyListLab['text'] = f'WeightList:{kList}'


def startThread():
    global randomizeFlag
    # GUI
    if len(kList) == len(wList) and len(kList) > 0 and len(kList) > 0:
        randomizeFlag = True
        startButt['state'] = DISABLED
        stopButt['state'] = ACTIVE
        setWeightButt['state'] = DISABLED
        setKeyButt['state'] = DISABLED
        removeWeightButt['state'] = DISABLED
        removeKeyButt['state'] = DISABLED

    else:
        return 0


def stopThread():
    global randomizeFlag
    randomizeFlag = False
    startButt['state'] = ACTIVE
    stopButt['state'] = DISABLED
    setWeightButt['state'] = ACTIVE
    setKeyButt['state'] = ACTIVE
    removeWeightButt['state'] = ACTIVE
    removeKeyButt['state'] = ACTIVE


weightListLab = Label(window, text=f'WeightList:{wList}')
weightInput = Entry(window, width=3)
setWeightButt = Button(window, text='Set', command=setWeight)
removeWeightButt = Button(window, text='Remove', command=popWeight)

keyListLab = Label(window, text=f'KeyList:{kList}')
keyInput = Entry(window, width=3)
setKeyButt = Button(window, text='Set', command=setKey)
removeKeyButt = Button(window, text='Remove', command=popKey)

startButt = Button(window, text='Start', command=startThread, state=ACTIVE)
stopButt = Button(window, text='Stop', command=stopThread, state=DISABLED)

window.geometry('320x240')

# window.config(background='gray')

weightListLab.grid(row=0, column=0)
weightInput.grid(row=0, column=1)
setWeightButt.grid(row=0, column=2)
removeWeightButt.grid(row=0, column=3)

keyListLab.grid(row=1, column=0)
keyInput.grid(row=1, column=1)
setKeyButt.grid(row=1, column=2)
removeKeyButt.grid(row=1, column=3)

startButt.grid(row=3, column=0)
stopButt.grid(row=3, column=1)
# mainThread = Thread(target=main)
mouseListener = mouseListener(on_click=onClick)
mouseListener.start()
# mainThread.start()
window.mainloop()
