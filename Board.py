import random


class Board:
    # creates a board that is n x n size
    def __init__(self, size):
        self.empty_symbol = 0
        self.board = [[self.empty_symbol for i in range(size)] for j in range(size)]

    # prints every row
    def display(self):
        for i in self.board:
            print i
        print

    # adds a 2 2's to empty squares
    def add_squares(self):
        # list with all empty coordinates left
        empty_cords = []

        # for every item in the board check if it is empty
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == self.empty_symbol:
                    empty_cords.append([i, j])

        # if there are not empty coordinates left then end the game
        if len(empty_cords) == 0:
            return
        # if there is one empty coordinate left then fill it
        if len(empty_cords) == 1:
            self.board[empty_cords[0][0]][empty_cords[0][1]] = 2

        # fill a random empty coordinate
        rand_index1 = int(random.uniform(0, len(empty_cords)))
        self.board[empty_cords[rand_index1][0]][empty_cords[rand_index1][1]] = 2

        # move that fill that coordinate with a coordinate that wasn't used before
        empty_cords[rand_index1] = empty_cords[-1]
        rand_index2 = int(random.uniform(0, len(empty_cords)-1))
        self.board[empty_cords[rand_index2][0]][empty_cords[rand_index2][1]] = 2

    def shift_board_right(self):
        # for every column except for the right most one and going leftwards
        for c in range(len(self.board[0])-2, -1, -1):
            # for every row going downwards
            for r in range(len(self.board)):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    while c+offset+1 <= len(self.board[r])-1:
                        # if the next right column is empty
                        if self.board[r][c+offset+1] == self.empty_symbol:
                            # fill it with the value
                            self.board[r][c+offset+1] = self.board[r][c+offset]
                            self.board[r][c+offset] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r][c+offset+1] == self.board[r][c+offset]:
                            # then add them together
                            self.board[r][c + offset + 1] += self.board[r][c + offset]
                            self.board[r][c + offset] = self.empty_symbol
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
                    while c-offset-1 >= 0:
                        # if the next right column is empty
                        if self.board[r][c-offset-1] == self.empty_symbol:
                            # fill it with the value
                            self.board[r][c-offset-1] = self.board[r][c-offset]
                            self.board[r][c-offset] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r][c-offset-1] == self.board[r][c-offset]:
                            # then add them together
                            self.board[r][c-offset-1] += self.board[r][c-offset]
                            self.board[r][c-offset] = self.empty_symbol
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
                    while r-offset-1 >= 0:
                        # if the next right column is empty
                        if self.board[r-offset-1][c] == self.empty_symbol:
                            # fill it with the value
                            self.board[r-offset-1][c] = self.board[r-offset][c]
                            self.board[r-offset][c] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r-offset-1][c] == self.board[r-offset][c]:
                            # then add them together
                            self.board[r-offset-1][c] += self.board[r-offset][c]
                            self.board[r-offset][c] = self.empty_symbol
                        else:
                            # then check the next row
                            break

    def shift_board_down(self):
        # for every row except for the bottom most one and going upwards
        for r in range(len(self.board)-2, -1, -1):
            # for every column going rightwards
            for c in range(len(self.board[r])):
                # if it is not empty
                if self.board[r][c] != self.empty_symbol:
                    # while the right most column exists
                    offset = 0
                    while r+offset+1 <= len(self.board)-1:
                        # if the next right column is empty
                        if self.board[r+offset+1][c] == self.empty_symbol:
                            # fill it with the value
                            self.board[r+offset+1][c] = self.board[r+offset][c]
                            self.board[r+offset][c] = self.empty_symbol
                            # check the next one to see if it is empty
                            offset += 1
                        # if there is something in the column and it is equal
                        elif self.board[r+offset+1][c] == self.board[r+offset][c]:
                            # then add them together
                            self.board[r+offset+1][c] += self.board[r+offset][c]
                            self.board[r+offset][c] = self.empty_symbol
                        else:
                            # then check the next row
                            break


game_board = Board(4)

for i in range(600):
    game_board.add_squares()
    game_board.shift_board_down()
    game_board.shift_board_left()
    game_board.shift_board_up()
    game_board.shift_board_right()
    game_board.display()