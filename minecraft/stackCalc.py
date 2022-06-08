from tkinter import *
from math import ceil
window = Tk()
window.title('Stack Calc')
window.geometry('520x180')

def calcBlock():
    try:
        inp = int(blockInput.get())
        block = inp%64
        stack = inp//64
        blockResultLabel['text'] = f'Stacks:{stack} , Blocks:{block} '
        print('death')
    except ValueError:
        print('not a number')

def calcRatio():
    try:
        x = float(ratioInput.get().split(':')[0])
        y = float(ratioInput.get().split(':')[1])
        block = int(ratioBlockInput.get())
        result = int(ceil(block/y)*x)
        remainder = int(((result/x)*y)-block)
        ratioResultLabel['text'] = f'Blocks:{int(ceil(block/y)*x)}, Excess:{remainder}'
        print(f'x:{x}, y:{y}')
    except ValueError:
        print('not an int')
    except IndexError:
        print('not proper format')
# stack calculator
blockLabel = Label(window, text='blocks', width=15)
blockInput = Entry(window, width=5)
blockCalcButt = Button(window, text='calculate!', command=calcBlock)
blockResultLabel = Label(window, text='Stacks:#, Blocks:#')

# ratio calculator
ratioLabel = Label(window, text='ratio(x:y)')
ratioInput = Entry(window, width=5)
ratioBlockLabel = Label(window, text='blocks:')
ratioBlockInput = Entry(window, width=5)
ratioCalcButt = Button(window, text='calculate!', command=calcRatio)
ratioResultLabel = Label(window, text='Blocks:#, Excess:#', width=15)

# Grid Placement
#  Stack Calculator
blockLabel.grid(row=0, column=0)
blockInput.grid(row=0, column=1)
blockCalcButt.grid(row=0, column=2)
blockResultLabel.grid(row=1, column=0)
#  Ratio Calculator
ratioLabel.grid(row=2, column=0)
ratioInput.grid(row=2, column=1)
ratioBlockLabel.grid(row=2, column=2)
ratioBlockInput.grid(row=2, column=3)
ratioCalcButt.grid(row=2, column=4)
ratioResultLabel.grid(row=3, column=0)

window.mainloop()