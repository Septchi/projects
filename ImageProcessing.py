import cv2 as cv

import numpy as np
import win32gui, win32ui, win32con

import time


class ImageProcessing:
    w = 0
    h = 0
    hwnd = None

    # Window Crop
    cropX = 0
    cropY = 0
    offsetX = 0
    offsetY = 0

    #inputArr = []
    threshold = 0

    def __init__(self, hwnd=None, window=None):
        # Initialized self variables
        # self.input = input
        # object detection variables
        self.threshold = 0.8
        self.appleImgTop = cv.imread("hello1.jpeg", cv.IMREAD_UNCHANGED)
        self.appleImgMid = cv.imread("hello2.jpeg", cv.IMREAD_UNCHANGED)
        self.appleImgBot = cv.imread("hello3.jpeg", cv.IMREAD_UNCHANGED)

        # Arrays
        self.cropArr = [[240, 180, 100, 100], [300, 180, 100, 100], [390, 180, 100, 100]]
        self.inputArr = []

        # self.hwnd = win32gui.FindWindow(None, window)
        self.hwnd = hwnd
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and title bar and cut them off
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropX = border_pixels
        self.cropY = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offsetX = window_rect[0] + self.cropX
        self.offsetY = window_rect[1] + self.cropY

    def screenshot(self):
        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropX, self.cropY), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        # dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel
        img = img[..., :3]
        img = np.ascontiguousarray(img)

        return img

    def identifyObject(self, template, index):
        # Identify Objects in the given Image
        result = cv.matchTemplate(template, self.appleImgTop, cv.TM_CCOEFF_NORMED)
        if index == 0:
            result = cv.matchTemplate(template, self.appleImgTop, cv.TM_CCOEFF_NORMED)
        elif index == 1:
            result = cv.matchTemplate(template, self.appleImgMid, cv.TM_CCOEFF_NORMED)
        elif index == 2:
            result = cv.matchTemplate(template, self.appleImgBot, cv.TM_CCOEFF_NORMED)
        minVal, maxVal, minPos, maxPos = cv.minMaxLoc(result)
        # print(maxVal)
        if maxVal > self.threshold:
            print("Detected", maxVal)
            if index == 0:
                # cv.imwrite("hello1.jpeg", template)
                input("w")
                self.inputArr.append("w")
            elif index == 1:
                # cv.imwrite("hello2.jpeg", template)
                self.inputArr.append("d")
            elif index == 2:
                # cv.imwrite("hello3.jpeg", template)
                self.inputArr.append("s")
            print(self.inputArr)

    def cropImage(self, arr, screenshot):
        # Crop original Screenshot to specific areas
        image = screenshot[arr[0]:arr[0] + arr[2], arr[1]:arr[1] + arr[3]]
        return image

    def processImage(self):
        # Process
        print("hello")
        while True:
            screenshot = self.screenshot()
            images = []
            for i in self.cropArr:
                # cv.imwrite("hello{}.jpeg".format(i), self.cropImage(i, screenshot))
                images.append(self.cropImage(i, screenshot))
            n = 0
            for i in images:
                # Bot cammands
                self.identifyObject(i, n)
                time.sleep(0.01)
                n += 1
            time.sleep(0.5)

    def listWindows(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)
