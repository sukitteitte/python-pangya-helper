from win32gui import *
from win32api import *
from win32con import *
import math
from time import sleep


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
    (cal_pixel) = abs(800 - abs(x))
    return cal_pixel


def get_calculator_pb():
    cal_pb = get_calculator_pixel() / 68
    return cal_pb


def get_position_screen(x, y):
    x_screen, y_screen = ClientToScreen(HWND(), (x, y))

    convertedPointX = x_screen * (65536 / 1919)
    convertedPointY = y_screen * (65536 / 1079)

    set_move = mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE, int(convertedPointX), int(convertedPointY), 0, 0)

    return set_move


def set_pb_move(pb):
    pixel = pb * 68
    pixel_final = 800 + pixel
    x_screen, y_screen = ClientToScreen(HWND(), (pixel_final, 450))
    convertedPointX = x_screen * (65536 / 1919)
    convertedPointY = y_screen * (65536 / 1079)

    set_move_pb = mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE, int(convertedPointX), int(convertedPointY), 0, 0)

    return set_move_pb


def mouse_client():
    x_screen, y_screen = ClientToScreen(HWND(), mousePosition())
    print(format("x={0},y={1}"), x_screen, y_screen)
