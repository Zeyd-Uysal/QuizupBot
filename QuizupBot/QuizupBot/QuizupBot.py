
from PIL import Image
import pytesseract
import argparse
import os
import win32api
import win32gui
import win32con
import time
import os
from pywinauto import Desktop, Application
import pyautogui
import threading


def main():
    runningGame()
    print(pytesseract.get_tesseract_version())
    gameStart()


def switch():
    hwnd = win32gui.FindWindow(None, 'Bluestacks')
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, 3)


def gameStart():
    switch()
    for x in range(2):
        time.sleep(1)
        pyautogui.click(findColor((2, 209, 116)))
    while isGameStarted() == False:
        print("loading")
        time.sleep(1)
    time.sleep(10)


def findColor(kleur):
    color = kleur
    s = pyautogui.screenshot()
    for x in range((s.width // 2), s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                return (x + 2, y + 2)
    return False


def isGameStarted():
    s = pyautogui.screenshot()
    for x in range(s.width // 2):
        for y in range(int(s.height * 0.30)):
            if s.getpixel((x, y)) == (250, 224, 66):
                return True
    return False


def quizBox():
    s = pyautogui.screenshot()
    x = int(s.width // 2.07)
    y = int(s.height * 0.85)
    if s.getpixel((x, y)) == (0, 0, 0):
        pyautogui.click(x, y)
        print("Black")
        return True
    pyautogui.click(x, y)
    return False


def runningGame():
    mode = quizBox()
    img = Image.open("test2.png")
    text = pytesseract.image_to_string(img)
    print(text)
def modes(mode):
    s = pyautogui.screenshot()
    if mode:

        return
    else:
        return
    return
if __name__ == "__main__":
    main()
