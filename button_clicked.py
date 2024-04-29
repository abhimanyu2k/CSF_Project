from tkinter import messagebox

turn = "X"
count = 0

def b_click(b):
    global turn, count
    if b["text"] == " " and turn == "X":
        b["text"] = turn
        turn = "O"
        count += 1
    elif b["text"] == " " and turn == "O":
        b["text"] = turn
        turn = "X"
        count += 1
    else:
        messagebox.showerror("Tic Tac Toe", "The Box was selected earlier. \n Pick another box!")
