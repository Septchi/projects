from tkinter import *
from PIL import ImageTk, Image
from os import getcwd
from functools import partial

cd = getcwd()

window = Tk()

window.title('death')
window.geometry('500x500')
window.iconbitmap('xaio.ico')
# constant variables
dropOffsetX = 115
dropOffsetY = 40
charOffsetX = 8
charOffsetY = 18
buttOffsetY = 26
maxChar = 48
tempList = ['particular', 'special', 'exclusive', 'privy', 'own', 'secluded']
colorList = ['red', 'red', 'orange', 'orange', 'yellow', 'yellow']
# global variables
charOffset = [0]
charPosX = 0
charPosY = 0
clickPos = []


# class shit
class death:
    def __init__(self):
        self.widgetList = []

    def insertButton(self, text, bg):
        self.widgetList.append(Button(text=text, relief='flat', bg=bg, command=partial(buttonShit, text)))


widgets = death()


# Functions
def inputClear(e):
    inputField.delete('1.0', END)


def buttonShit(text):
    print(text)
    inpSentence = inputField.get('1.0', END).strip()
    words = inpSentence.split(' ')
    for i, word in enumerate(words):
        if word == 'personal':
            print('found')
            words[i] = text
    inpBuffer = ''.join([f'{word} ' for word in words])
    inputField.delete('1.0', END)
    inputField.insert(END, inpBuffer.strip())
    for widget in widgets.widgetList:
        widget.place_forget()


def mousePress(e):
    x = window.winfo_pointerx() - window.winfo_rootx()
    y = window.winfo_pointery() - window.winfo_rooty()
    for pos1, pos2 in clickPos:
        if (pos2[0] >= x >= pos1[0]) and (pos1[1] >= y >= pos2[1]):
            print('hello')
            for i, widget in enumerate(widgets.widgetList):
                widget.place(x=pos1[0], y=pos1[1] + (buttOffsetY * i))
            break


def placeWidget(x, y, text):
    dummyString = ''
    indexList = []
    charCount = 0

    for i, word in enumerate(tempList):
        dummyString += f'{word}\n'
        charCount += len(word)
        if i == 0:
            indexList.append([0, charCount-1])
        else:
            indexList.append([indexList[i-1][1]+1, charCount-1])
    for i, widget in enumerate(widgets.widgetList):
        pass
        # widget.place(x=x, y=y + (charOffsetY * i))
    # dummyLabel['text'] = dummyString.strip()
    # dummyLabel.place(x=x, y=y)


def inputEnter(e):
    global charPosX, charPosY
    clickPos.clear()
    charPosX, charPosY = 0, 0
    inpSentence = inputField.get('1.0', END).strip()
    inputField.delete('1.0', END)
    inputField.insert(END, inpSentence)
    words = inpSentence.split(' ')
    for i, iword in enumerate(words):
        if iword == 'personal':
            for j, jword in enumerate(words):
                charPosX += len(jword)+1 if j < i else 0
            x = dropOffsetX + (charOffsetX * (charPosX - charOffset[-1]))
            for i, offset in enumerate(charOffset[::-1]):
                if charPosX >= offset:
                    charPosY = i + 1
                    break
            y = dropOffsetY + (charOffsetY * charPosY)
            clickPos.append([[x, y], [x + (charOffsetX * len(iword)), y-charOffsetY]])
    print(f'charPos:{charPosX - charOffset[-1]}, clickPos:{clickPos}')
    placeWidget(dropOffsetX + (charOffsetX * charPosX), dropOffsetY + (charOffsetY * charPosY), inputField)

def inputPress(e):
    print('hello')
    inpSetence = inputField.get('1.0', END).strip()
    inputField.delete('1.0', END)
    inputField.insert(END, inpSetence)


def inputRelease(e):
    global charOffset
    inpSentence = inputField.get('1.0', END).strip()
    words = inpSentence.split(' ')
    wordCount = len(words[-1])
    charCount = len(inpSentence)
    if charOffset[-1] + 1 >= charCount:
        if len(charOffset) > 1:
            charOffset.pop(-1)
    if charCount > maxChar + charOffset[-1] and wordCount < maxChar:
        currWord = words.pop(-1)
        # inputField.delete('1.0', END)
        inpBuffer = ''.join([f'{word} ' for word in words])
        charOffset.append(len(inpBuffer))
        inpBuffer += f'\n{currWord}'
        # inputField.delete('1.0', END)
        # inputField.insert(END, inpBuffer.strip())
    print(f'charCount:{charCount}, wordCount{wordCount}, charOffset:{charOffset}, currWord:{words[-1].strip()}')


# instantiate widgets
sidebar = Frame(window)
dummyImage = ImageTk.PhotoImage(Image.open(cd+'/xaio.jpg').resize((50, 50), Image.ANTIALIAS))
dictIcon = Label(sidebar, image=dummyImage)
dictionary = Label(sidebar, text='dictionary')
thesIcon = Label(sidebar, image=dummyImage)
thesaurus = Label(sidebar, text='thesaurus')
saveIcon = Label(sidebar, image=dummyImage)
saveFile = Label(sidebar, text='save file')
newIcon = Label(sidebar, image=dummyImage)
newFile = Label(sidebar, text='new file')
openIcon = Label(sidebar, image=dummyImage)
openFile = Label(sidebar, text='open file')

inputField = Text(window, width=48, height=20, relief='flat', wrap=WORD)
inputField.insert(END, 'Type sentences here...')
inputField.bind('<FocusIn>', inputClear)
inputField.bind('<Return>', inputEnter)
inputField.bind('<Button>', mousePress)
inputField.bind('<KeyPress>', inputPress)
inputField.bind('<KeyRelease>', inputRelease)
clicked = StringVar()

dummyLabel = OptionMenu(window, clicked, *tempList)

# place widgets
sidebar.grid(row=0, column=0, pady=(50, 0))

dictIcon.grid(row=0, column=0)
dictionary.grid(row=0, column=1)
thesIcon.grid(row=1, column=0)
thesaurus.grid(row=1, column=1)
saveIcon.grid(row=2, column=0)
saveFile.grid(row=2, column=1)
newIcon.grid(row=3, column=0)
newFile.grid(row=3, column=1)
openIcon.grid(row=4, column=0)
openFile.grid(row=4, column=1)

inputField.grid(row=0, column=1, sticky='nw', pady=(20, 0))


def main():
    for i, (word, color) in enumerate(zip(tempList, colorList)):
        widgets.insertButton(word, color)
    window.mainloop()


if __name__ == '__main__':
    main()
