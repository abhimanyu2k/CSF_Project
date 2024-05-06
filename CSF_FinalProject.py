## CompSci Foundations - Final project
## Tic Tac Toe
## Abhimanyu Barun, Alice Pascalev, Sabrina Pierre

#Importing packages
import tkinter
from tkinter import *
import tkinter.messagebox as msg

#Initializing window
root= Tk()
root.title('TIC-TAC-TOE')

digits = [1,2,3,4,5,6,7,8,9]
mark = '' 
count = 0
panels = ["panel"]*10