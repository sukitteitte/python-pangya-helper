import win32gui, win32api, win32con, win32console, win32process
import math
import time
import pyautogui


# Pangya Fresh Up!
# print("X:" + str(x) + "," + "Y:" + str(y))

def cursor():
    while True:
        (screenX, screenY) = pyautogui.size()
        (x, y) = win32gui.GetCursorPos()
        (angelX, angelY) = (x - (screenX / 2), y - (screenY / 2))
        angel = math.degrees((math.atan2(abs(angelY), abs(angelX))))
        # angel = math.degrees((math.atan2(angelY, angelX)))
        time.sleep(0.05)
        print("Angel: %.2f" % angel)

        # pyautogui.moveTo(960,540)


cursor()

# def screenPangya():
#     while True:
#         hwnd = win32gui.FindWindow(None, "Pangya Fresh Up!")
#         rect = win32gui.GetWindowRect(hwnd)
#         (cursorX, cursorY) = win32gui.GetCursorPos()
#         (posX, posY) = win32gui.ScreenToClient(hwnd, (cursorX, cursorY))
#         # print("posX:" + str(posX) + "," + "posY:" + str(posY))
#         # x = rect[0]
#         # y = rect[1]
#         # w = rect[2] - x
#         # h = rect[3] - y
#
#         (angelX, angelY) = (posX - ( 800/ 2), posY - (600 / 2))
#         angle = math.degrees((math.atan2(angelY, angelX)))
#         print("Angel: %.2f" % angle)
#         # print("\t    Size: (%d, %d)" % (w, h))
#
#
# screenPangya()
