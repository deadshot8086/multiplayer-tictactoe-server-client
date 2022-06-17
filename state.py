# Stores game state like board, turn...
from helper import send, State


class GameState:
    def __init__(self, n):
        self.isRunning = True
        self.turn = 0
        self.board_size = n
        self.board = [[' ' for x in range(self.board_size)] for y in range(self.board_size)]
        # row count +1*X-1*Y for a row
        self.row = [0 for x in range(self.board_size)]
        # col count +1*X-1*Y for a col
        self.col = [0 for x in range(self.board_size)]
        # diagonal count +1*X-1*Y for both diagonals
        self.diag = [0, 0]
        # total number of X, O in board
        self.mark_count = 0
        self.winner = None
        self.loser = None
        self.draw = False

    # Function to change turn after successful move
    def flip_turn(self):
        self.turn = not self.turn

    # moves player on x, y on board
    def move(self, player, x, y):
        # for a in self.board:
        #     print(a)
        # valid condition check
        if 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[x][y] == ' ':
            # update board, mark_count, row, col, diagonal
            self.board[x][y] = player.mark
            self.mark_count += 1
            self.row[x] += 1 if player.mark == 'X' else -1
            self.col[y] += 1 if player.mark == 'X' else -1
            if x == y:
                self.diag[0] += 1 if player.mark == 'X' else -1
            if self.board_size - x - 1 == y:
                self.diag[1] += 1 if player.mark == 'X' else -1
            # check for win state using row, col, diagonal associated with that move
            if (abs(self.row[x]) == self.board_size or abs(self.col[x]) == self.board_size
                    or abs(self.diag[0]) == self.board_size or abs(self.diag[1]) == self.board_size):
                return State.WIN
            # check for draw if all filled
            if self.mark_count == pow(self.board_size, 2):
                return State.DRAW
            self.flip_turn()
            return 1
        # return 0 if unsuccessful
        return 0
