from tkinter import *
from grid1 import *
from grid1 import grid9


root = Tk()
root.geometry("500x500")
root.title("TIC - TAC - TOE")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text = "TIC TAC TOE")
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()
grid9(frame2)


root.mainloop()


