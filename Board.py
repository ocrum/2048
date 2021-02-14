from tkinter import Tk, Label
import random


# This is a matrix of the board that stores all the information in the simplest form meaning no GUI stuff
class Board:
    # creates a board that is n x n size
    def __init__(self, size):
        self.empty_symbol = 0
        self.board = [[self.empty_symbol for _ in range(size)] for _ in range(size)]
        self.score = 0

    # prints every row
    def print(self):
        for i in self.board:
            print(i)
        print()

    # adds a 2 or a 4 to two empty squares
    def add_squares(self):
        # list with all empty coordinates left
        empty_cords = []

        # for every item in the board check if it is empty
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.empty_symbol:
                    empty_cords.append([i, j])

        if random.random() < 0.1:
            random_num1 = 4
        else:
            random_num1 = 2

        if random.random() < 0.1:
            random_num2 = 4
        else:
            random_num2 = 2

        # if there are not empty coordinates left then end the game
        if len(empty_cords) == 0:
            return
        # if there is one empty coordinate left then fill it
        elif len(empty_cords) == 1:
            self.board[empty_cords[0][0]][empty_cords[0][1]] = random_num1
            return
        else:
            # fill a random empty coordinate
            rand_index1 = int(random.uniform(0, len(empty_cords)))
            self.board[empty_cords[rand_index1][0]][empty_cords[rand_index1][1]] = random_num1

            # move that fill that coordinate with a coordinate that wasn't used before
            empty_cords[rand_index1] = empty_cords[-1]
            rand_index2 = int(random.uniform(0, len(empty_cords) - 1))
            self.board[empty_cords[rand_index2][0]][empty_cords[rand_index2][1]] = random_num2

    # create a preset
    def preset(self):
        self.board[0][0] = 8
        self.board[1][0] = 4
        self.board[2][0] = 2
        self.board[3][0] = 2

    def shift_board_right(self):
        # for every column except for the right most one and going leftwards
        for c in range(len(self.board[0]) - 2, -1, -1):
            # for every row going downwards
            for r in range(len(self.board)):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    while c + offset + 1 <= len(self.board[r]) - 1:
                        # if the next right column is empty
                        if self.board[r][c + offset + 1] == self.empty_symbol:
                            # fill it with the value
                            self.board[r][c + offset + 1] = self.board[r][c + offset]
                            self.board[r][c + offset] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r][c + offset + 1] == self.board[r][c + offset]:
                            # then add them together
                            self.board[r][c + offset + 1] += self.board[r][c + offset]
                            self.board[r][c + offset] = self.empty_symbol
                            # add the score
                            self.score += self.board[r][c + offset + 1]
                        else:
                            # then check the next row
                            break

    def shift_board_left(self):
        # for every column except for the left most one and going rightwards (changed)
        for c in range(1, len(self.board[0]), 1):
            # for every row going downwards
            for r in range(len(self.board)):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    # changed
                    while c - offset - 1 >= 0:
                        # if the next right column is empty
                        if self.board[r][c - offset - 1] == self.empty_symbol:
                            # fill it with the value
                            self.board[r][c - offset - 1] = self.board[r][c - offset]
                            self.board[r][c - offset] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r][c - offset - 1] == self.board[r][c - offset]:
                            # then add them together
                            self.board[r][c - offset - 1] += self.board[r][c - offset]
                            self.board[r][c - offset] = self.empty_symbol
                            # add the score
                            self.score += self.board[r][c - offset - 1]
                        else:
                            # then check the next row
                            break

    def shift_board_up(self):
        # for every row except for the top most one and going downwards
        for r in range(1, len(self.board), 1):
            # for every column going rightwards
            for c in range(len(self.board[r])):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    while r - offset - 1 >= 0:
                        # if the next right column is empty
                        if self.board[r - offset - 1][c] == self.empty_symbol:
                            # fill it with the value
                            self.board[r - offset - 1][c] = self.board[r - offset][c]
                            self.board[r - offset][c] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r - offset - 1][c] == self.board[r - offset][c]:
                            # then add them together
                            self.board[r - offset - 1][c] += self.board[r - offset][c]
                            self.board[r - offset][c] = self.empty_symbol
                            # add the score
                            self.score += self.board[r - offset - 1][c]
                        else:
                            # then check the next row
                            break

    def shift_board_down(self):
        # for every row except for the bottom most one and going upwards
        for r in range(len(self.board) - 2, -1, -1):
            # for every column going rightwards
            for c in range(len(self.board[r])):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    while r + offset + 1 <= len(self.board) - 1:
                        # if the next right column is empty
                        if self.board[r + offset + 1][c] == self.empty_symbol:
                            # fill it with the value
                            self.board[r + offset + 1][c] = self.board[r + offset][c]
                            self.board[r + offset][c] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r + offset + 1][c] == self.board[r + offset][c]:
                            # then add them together
                            self.board[r + offset + 1][c] += self.board[r + offset][c]
                            self.board[r + offset][c] = self.empty_symbol
                            # add the score
                            self.score += self.board[r + offset + 1][c]
                        else:
                            # then check the next row
                            break


# take in a key event and then does certain action based on that
def key_handler(event):
    if event.keysym == 'Up':
        game_board.shift_board_up()
    elif event.keysym == 'Down':
        game_board.shift_board_down()
    elif event.keysym == 'Left':
        game_board.shift_board_left()
    elif event.keysym == 'Right':
        game_board.shift_board_right()
    else:
        # if it is not a used key it will print something in the console
        print('Useless Key: ', event.keysym)
        return
    # add the scores
    game_board.add_squares()

    # update the GUI board
    score.config(text="Score: " + str(game_board.score))
    for i in range(4):
        for j in range(4):
            if game_board.board[i][j] == 0:
                tkinter_board[i][j].config(text='')
            else:
                tkinter_board[i][j].config(text=game_board.board[i][j])


# basic Tkinter set up
root = Tk()
root.title('2048')
root.bind('<Key>', key_handler)
game_board = Board(4)
# holds all of the Tkinter widgets
tkinter_board = []
# add squares when the game starts
game_board.add_squares()
game_board.preset()

# add the score label
score = Label(root, text="Score: " + str(game_board.score))
score.grid(row=0, column=0, columnspan=4)

# creates all of the widgets and puts them into the tkinter_board matrix
for i in range(4):
    rows = []
    for j in range(4):
        tile = Label(root, text='' if game_board.board[i][j] == 0 else game_board.board[i][j]
                     , height=2, width=4, borderwidth=5, relief="groove")
        tile.grid(row=i + 1, column=j)
        rows.append(tile)
    tkinter_board.append(rows)

root.mainloop()
