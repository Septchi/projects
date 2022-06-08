import numpy as np
import cv2
from time import time
import win32gui
from ImageProcessing import ImageProcessing
from Bot import Bot
window = "SuperNova - https://chat.kongregate.com/gamez/0024/9627/live/game.swf?kongregate_game_version=1564415602"
hwnd = win32gui.FindWindow(None, window)
imgProc = ImageProcessing(hwnd)
bot = Bot()
points = ((250, 250), (280, 350), (270, 425))
loopTime=0

inputBuffer = 0.1
startW = 0
startD = 0
startS = 0


def test(hay, sqrList):
    needle = cv2.imread("apple.jpeg", 0)
    result = cv2.matchTemplate(hay, needle, cv2.TM_CCOEFF_NORMED)

    needleW = needle.shape[1]
    needleH = needle.shape[0]

    threshold = 0.52


    locations = np.where(result>=threshold)
    locations = list(zip(*locations[::-1]))

    min, max, minPos, maxPos = cv2.minMaxLoc(result)

    res = min
    resPos = minPos


    rects = []

    if locations:

        for location in locations:
            rect = [int(location[0]), int(location[1]), needleW, needleH]
            rects.append(rect)

        rects, weights = cv2.groupRectangles(rects, groupThreshold=1, eps=0.5)
        if len(rects):
            for (x, y, w, h) in rects:
                topLeft = (x, y)
                botRight = (x + w, y + h)
                checkHit(sqrList, topLeft, botRight)
                cv2.rectangle(hay, topLeft, botRight, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)
    return hay

class rect():
    def __init__(self, center, width, length):
        self.p1 = (center[0] - (width // 2), center[1] - (length // 2))
        self.p2 = (center[0] + (width // 2), center[1] + (length // 2))

def checkHit(sqrList, p1, p2):
    global inputBuffer, startW, startD, startS
    for sqr in sqrList:
        if (sqr.p1[0]>=p1[0] and sqr.p1[1]>=p1[1]) and (sqr.p2[0]<=p2[0] and sqr.p2[1]<=p2[1]) and sqr == sqrList[0] and time()-startW>=inputBuffer:
            print('hit found in W')
            bot.input('w')
            startW = time()
        if (sqr.p1[0]>=p1[0] and sqr.p1[1]>=p1[1]) and (sqr.p2[0]<=p2[0] and sqr.p2[1]<=p2[1]) and sqr == sqrList[1] and time()-startD>=inputBuffer:
            print('hit found in D')
            bot.input('d')
            startD = time()
        if (sqr.p1[0]>=p1[0] and sqr.p1[1]>=p1[1]) and (sqr.p2[0]<=p2[0] and sqr.p2[1]<=p2[1]) and sqr == sqrList[2] and time()-startS>=inputBuffer:
            print('hit found in S')
            bot.input('s')
            startS = time()
def main():
    sqrList = []
    for point in points:
        sqrList.append(rect(point, 4, 4))

    global img

    while True:
        global loopTime
        print("FPS: {}".format(1 / (time() - loopTime)))
        loopTime = time()


        img = test(cv2.cvtColor(imgProc.screenshot(),cv2.COLOR_RGB2GRAY), sqrList)
        #draw recatangles
        for sqr in sqrList:
            cv2.rectangle(img, sqr.p1, sqr.p2, (255, 255, 255))

        cv2.imshow("Test", img)
        cv2.waitKey(1)
        # if(cv2.waitKey(1) & 0xFF) == ord('s'):
        #     cv2.imwrite("screen.jpeg", img)
        #
        # if (cv2.waitKey(1) & 0xFF) == ord('q'):
        #     cv2.destroyAllWindows()
        #     break

# Start of the main program here
if __name__ == "__main__":
    #test()
    #bot.start()
    main()
