from Board import Board
import tkinter as tk


# TODO Make something display on the tkinter window
def display_array(arr):
    return arr


root = tk.Tk()
root.geometry('400x400')
root.title("2048 Game")

C = tk.Canvas(root, width=300, height=300, highlightthickness=5, highlightbackground="black")
C.grid(row=0, column=0)
C.create_rectangle(50, 0, 100, 50, fill='red')

game_board = Board(4)

for i in range(600):
    game_board.add_squares()
    game_board.shift_board_down()
    game_board.shift_board_left()
    game_board.shift_board_up()
    game_board.shift_board_right()
    game_board.print()
    display_array(game_board.board)

# this is the loop
root.mainloop()
