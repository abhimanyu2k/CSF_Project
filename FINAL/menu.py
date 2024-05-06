from main import *
from main import twoPlayer
from one_player import onePlayer

def play():
    menu = Tk()
    menu.geometry("500x500")
    menu.title("Tic Tac Toe")

    head = Label(menu, text = "TIC TAC TOE", width = 500)
    B1plyr = Button(menu, text="Single Player", command = onePlayer, width=500)
    B2plyr = Button(menu, text="Two Player", command = twoPlayer, width=500)
    Bexit = Button(menu, text="Exit", command = menu.quit, width=500)
    head.pack(side='top')
    B1plyr.pack(side='top')
    B2plyr.pack(side='top')
    Bexit.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()