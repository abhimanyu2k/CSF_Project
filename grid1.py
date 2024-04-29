# Build the grid
# The grid will have 9 buttons

from tkinter import *
from button_clicked import b_click


def grid9(frame2):
    b1 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b1))
    b2 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b2))
    b3 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b3))

    b4 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b4))
    b5 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b5))
    b6 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b6))

    b7 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b7))
    b8 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b8))
    b9 = Button(frame2, text = " ", height = 3, width = 6, command= lambda: b_click(b9))

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)

    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)

    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

