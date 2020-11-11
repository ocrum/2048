# from Board import Board
import tkinter as tk


# game_board = Board(4)
root = tk.Tk()

# creating a label widget
myLabel1 = tk.Label(root, text="Hello World!")
myLabel2 = tk.Label(root, text="My name is pee pee poopie!")

# shoving it into the window
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# this is the loop
root.mainloop()
