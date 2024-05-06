
#%%
from tkinter import *
from tkinter import messagebox
import random

### Setting up the grid to make up the game board

global b1, b2, b3, b4, b5, b6, b7, b8, b9
def grid9(frame2):

    global b1, b2, b3, b4, b5, b6, b7, b8, b9

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

turn = "X"
count = 0

### Setting up the game so the one player starts with placing an X on the board. For each move, the program is checking for winning combinations on the board. If a player tries to place an X where there is already a symbol, an error message will show. 

def computer_move():
    global turn, count
    available_buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    empty_buttons = [button for button in available_buttons if button["text"] == " "]
    if empty_buttons:
        computer_choice = random.choice(empty_buttons)
        computer_choice["text"] = turn
        turn = "X"
        count += 1
        checkifwon()

def b_click(b):
    global turn, count
    if b["text"] == " " and turn == "X":
        b["text"] = turn
        turn = "O"
        count += 1
        checkifwon()
        if winner is False:
            computer_move()

    elif b["text"] == " " and turn == "O":
        b["text"] = turn
        turn = "X"
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "The Box was selected earlier. \n Pick another box!")

def checkifwon():
    global winner
    winner = False
    if (
        b1["text"] == b2["text"] == b3["text"] == "X" or
        b4["text"] == b5["text"] == b6["text"] == "X" or
        b7["text"] == b8["text"] == b9["text"] == "X" or
        b1["text"] == b4["text"] == b7["text"] == "X" or
        b2["text"] == b5["text"] == b8["text"] == "X" or
        b3["text"] == b6["text"] == b9["text"] == "X" or
        b1["text"] == b5["text"] == b9["text"] == "X" or
        b3["text"] == b5["text"] == b7["text"] == "X"
    ):
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
        disable_all_buttons()
    elif (
        b1["text"] == b2["text"] == b3["text"] == "O" or
        b4["text"] == b5["text"] == b6["text"] == "O" or
        b7["text"] == b8["text"] == b9["text"] == "O" or
        b1["text"] == b4["text"] == b7["text"] == "O" or
        b2["text"] == b5["text"] == b8["text"] == "O" or
        b3["text"] == b6["text"] == b9["text"] == "O" or
        b1["text"] == b5["text"] == b9["text"] == "O" or
        b3["text"] == b5["text"] == b7["text"] == "O"
    ):
        winner = True
        messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
        disable_all_buttons()
    elif count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
        disable_all_buttons()

### This code ensures the structure and presence of the window after every move. It also makes sure the game is destroyed once a tie or winner is called so that another game can be played from scratch once more. 

def disable_all_buttons():
    global turn, count
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
    turn = "X"
    count = 0
    root.destroy()

def onePlayer():
    global root
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

