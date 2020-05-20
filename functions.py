from win32gui import *
from win32api import *
from win32con import *
from time import sleep
import math


def HWND():
    hwnd = FindWindow(None, "Pangya Fresh Up!")
    # print("HWND : {0}", hwnd)
    return hwnd


def mousePosition():
    (x_mouse, y_mouse) = GetCursorPos()
    # print("X: {0} , Y: {1} ", x_mouse, y_mouse)
    return x_mouse, y_mouse


def pangyaPosition():
    (x_pangya, y_pangya) = ScreenToClient(HWND(), mousePosition())
    # print(x_pangya, y_pangya)
    return x_pangya, y_pangya


def degree():
    (x, y) = pangyaPosition()
    (x_axis, y_axis) = (x - (1600 / 2), y - (900 / 2))
    degree_wind = math.degrees((math.atan2(abs(y_axis), abs(x_axis))))
    return degree_wind


def get_degree_90():
    angle90 = 90 - degree()
    return angle90


def get_degree_0():
    angle0 = degree()
    return angle0


def get_calculator_pixel():
    (x, y) = pangyaPosition()
    cal_pixel = 800 - abs(x)
    return cal_pixel


def get_calculator_pb():
    cal_pb = get_calculator_pixel() / 68
    return cal_pb


def get_position_screen(x, y):
    x_screen, y_screen = ClientToScreen(HWND(), (x, y))
    set_move = SetCursorPos((x_screen, y_screen))
    return set_move
