from tkinter import *
from tkinter.font import Font
import win32gui
import math
import time


class App(Tk):
    def __init__(self):
        self.gui = Tk()
        self.gui.title("pyAngleBeta ver 0.0.1")
        self.gui.iconbitmap(r"wind.ico")
        self.font = Font(family="Roboto", size=20, weight="bold")

        Label(self.gui, text="xPOS : ", font=self.font).grid(row=0)
        self.x_pos = DoubleVar()
        Label(self.gui, textvariable=self.x_pos, font=self.font).grid(row=0, column=1)

        Label(self.gui, text="yPOS : ", font=self.font).grid(row=1)
        self.y_pos = DoubleVar()
        Label(self.gui, textvariable=self.y_pos, font=self.font).grid(row=1, column=1)

        Label(self.gui, text="Degree : ", font=self.font).grid(row=2)
        self.degree_pos = DoubleVar()
        Label(self.gui, textvariable=self.degree_pos, font=self.font).grid(row=2, column=1)

        # # Screen PangYa Get Position
        # hwnd = win32gui.FindWindow(None, "Pangya Fresh Up!")
        # while True:
        #     (cursorX, cursorY) = win32gui.GetCursorPos()
        #     (x, y) = win32gui.ScreenToClient(hwnd, (cursorX, cursorY))
        #     (angelX, angelY) = (x - (1600 / 2), y - (900 / 2))
        #     angle = math.degrees((math.atan2(abs(angelY), abs(angelX))))
        #
        #     self.x_pos.set(x)
        #     self.y_pos.set(y)
        #     self.degree_pos.set("%.2f" % angle)
        #     time.sleep(0.005)
        #     self.gui.update()

        # Screen Windows Get Position
        while True:
            (x, y) = win32gui.GetCursorPos()
            (angelX, angelY) = (x - (1920 / 2), y - (1080 / 2))
            angle = math.degrees((math.atan2(abs(angelY), abs(angelX))))

            self.x_pos.set(x)
            self.y_pos.set(y)
            self.degree_pos.set("%.2f" % angle)
            time.sleep(0.005)
            self.gui.update()


App()
