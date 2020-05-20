from tkinter import *
from tkinter.font import Font
from win32gui import *
from win32api import *
from win32con import *
from functions import *
from time import sleep
import math


class App(Tk):
    def __init__(self):
        self.gui = Tk()
        gui = self.gui
        gui.title("Pangya Project Version 1.0.0")
        gui.resizable(False, False)
        gui.heading1 = Font(family="Roboto", size=14)
        gui.heading2 = Font(family="Roboto", size=12)
        gui.heading3 = Font(family="Roboto", size=10, weight="bold")

        Label(gui, text="position", font=gui.heading1).grid(row=0, column=0, padx=20)

        Label(gui, text="x", font=gui.heading2).grid(row=1, column=0)
        self.x_pos = IntVar()
        Label(gui, textvariable=self.x_pos, font=gui.heading2, width=5).grid(row=1, column=1, padx=30)

        Label(gui, text="y", font=gui.heading2).grid(row=2, column=0)
        self.y_pos = IntVar()
        Label(gui, textvariable=self.y_pos, font=gui.heading2).grid(row=2, column=1)

        Label(gui, text="degree", font=gui.heading1).grid(row=3, column=0)

        Label(gui, text="90°", font=gui.heading2).grid(row=4, column=0)
        self.degree_90 = IntVar()
        Label(gui, textvariable=self.degree_90, font=gui.heading2).grid(row=4, column=1)

        Label(gui, text="0°", font=gui.heading2).grid(row=5, column=0)
        self.degree_0 = IntVar()
        Label(gui, textvariable=self.degree_0, font=gui.heading2).grid(row=5, column=1)

        Label(gui, text="calculator", font=gui.heading1).grid(row=6, column=0)

        Label(gui, text="pb", font=gui.heading2).grid(row=7, column=0)
        self.pb = IntVar()
        Label(gui, textvariable=self.pb, font=gui.heading2).grid(row=7, column=1)

        Label(gui, text="pixel", font=gui.heading2).grid(row=8, column=0)
        self.pixel = IntVar()
        Label(gui, textvariable=self.pixel, font=gui.heading2).grid(row=8, column=1)

        Label(gui, text="spin", font=gui.heading2).grid(row=9, column=0)
        self.spin = IntVar()
        Label(gui, textvariable=self.spin, font=gui.heading2).grid(row=9, column=1)

        Label(gui, text="curve", font=gui.heading2).grid(row=10, column=0)
        self.curve = IntVar()
        Label(gui, textvariable=self.curve, font=gui.heading2).grid(row=10, column=1)

        Label(gui, text="pb/4", font=gui.heading2).grid(row=7, column=3)
        self.pb_divide = DoubleVar()
        Entry(gui, textvariable=self.pb_divide, font=gui.heading2, width=5).grid(row=7, column=4)
        Button(gui, text="ans", command=self.cal, font=gui.heading2).grid(row=7, column=5, padx=20)
        self.pb_divide_cal = IntVar()
        Label(gui, textvariable=self.pb_divide_cal, font=gui.heading2).grid(row=8, column=4)

        # coming soon!
        # Label(gui, text="Slope", font=gui.heading2).grid(row=9, column=0)

        Label(gui, text="move help", font=gui.heading1).grid(row=0, column=3)

        Label(gui, text="spin", font=gui.heading2).grid(row=1, column=3)
        self.set_spin = IntVar()
        Entry(gui, textvariable=self.set_spin, font=gui.heading2, width=5).grid(row=1, column=4)
        Button(gui, text="Move", font=gui.heading2, command=self.move_spins).grid(row=1, column=5)

        Label(gui, text="curve", font=gui.heading2).grid(row=2, column=3)
        self.set_curve = IntVar()
        Entry(gui, textvariable=self.set_curve, font=gui.heading2, width=5).grid(row=2, column=4)
        Button(gui, text="Move", font=gui.heading2).grid(row=2, column=5)

        Label(gui, text="pixel", font=gui.heading2).grid(row=3, column=3)
        self.set_pixel = IntVar()
        Entry(gui, textvariable=self.set_pixel, font=gui.heading2, width=5).grid(row=3, column=4)
        Button(gui, text="Move", font=gui.heading2).grid(row=3, column=5)

        Label(gui, text="pb", font=gui.heading2).grid(row=4, column=3)
        self.set_pb = IntVar()
        Entry(gui, textvariable=self.set_pb, font=gui.heading2, width=5).grid(row=4, column=4)
        Button(gui, text="Move", font=gui.heading2).grid(row=4, column=5)

        Label(gui, text="by@TENDEV", font=gui.heading3).grid(row=11, column=5)

        while True:
            (x, y) = pangyaPosition()

            self.x_pos.set(x)
            self.y_pos.set(y)
            self.degree_90.set("%.2f" % get_degree_90())
            self.degree_0.set("%.2f" % get_degree_0())
            self.pb.set("%.2f" % get_calculator_pb())
            self.pixel.set("%.2f" % get_calculator_pixel())

            if (x, y) == (309, 790):
                self.spin.set(0)
            elif (x, y) == (309, 805):
                self.spin.set(8)
            elif (x, y) == (309, 807):
                self.spin.set(8)
            elif (x, y) == (309, 809):
                self.spin.set(8)
            elif (x, y) == (309, 810):
                self.spin.set(10)
            elif (x, y) == (309, 812):
                self.spin.set(11)
            elif (x, y) == (309, 846):
                self.spin.set(39)
            elif (x, y) == (309, 848):
                self.spin.set(30)
            else:
                self.spin.set(0)

            sleep(0.0005)
            gui.update()

    def move_spins(self):
        set_spin = (self.set_spin.get())
        if set_spin == 0:
            get_position_screen(309, 790)
        elif set_spin == 7:
            get_position_screen(309, 805)
        elif set_spin == 8:
            get_position_screen(309, 807)
        elif set_spin == 9:
            get_position_screen(309, 809)
        elif set_spin == 10:
            get_position_screen(309, 810)
        elif set_spin == 11:
            get_position_screen(309, 812)
        elif set_spin == 30:
            get_position_screen(309, 846)
        elif set_spin == 30:
            get_position_screen(309, 848)

    # def move_curve(self):
    #
    # def move_pixel(self):
    #
    # def move_pb(self):

    def cal(self):
        get_pb = (self.pb_divide.get())
        get_pb_divide = (get_pb / 4)
        self.pb_divide_cal.set("%.2f" % get_pb_divide)


App()
