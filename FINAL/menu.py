from main import *
from main import twoPlayer
from one_player import onePlayer

def play():
    menu = Tk()
    menu.geometry("500x500")
    menu.title("Tic Tac Toe")

    head = Label(menu, text = "★ Tic Tac Toe ★", width = 500, activeforeground='white',
				activebackground="#49D0F0", bg="#90D9EA",
				fg="#FF4F00", width=500, font='hobostd', bd=2)
    B1plyr = Button(menu, text="One Player", command = onePlayer, activeforeground='white',
				activebackground="#49D0F1", bg="#90D9EA",
				fg="#08A8D3", width=500, font='corbelbold', bd=2)
    B2plyr = Button(menu, text="Two Player", command = twoPlayer, activeforeground='white',
				activebackground="#49D0F1", bg="#90D9EA", fg="#08A8D3",
				width=500, font='corbelbold', bd=2)
    Bexit = Button(menu, text="Exit", command = menu.quit, width=500, activeforeground='white',
				activebackground="#49D0F1", bg="#90D9EA", fg="#08A8D3",
				font='corbelbold', bd=2)
    head.pack(side='top')
    B1plyr.pack(side='top')
    B2plyr.pack(side='top')
    Bexit.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()