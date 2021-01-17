from enum import Enum
import random
import copy

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Board:
    def __init__(self, width):
        self._width = width
        self._board = [[None] * width for _ in range(width)]

    def slide(self, dir):
        success = False
        if dir == Direction.LEFT:
            for i, r in enumerate(self._board):
                orig = r.copy()
                new_row = self._slide_a_row(r)
                if orig != new_row:
                    success = True
                    self._board[i] = new_row
        elif dir == Direction.RIGHT:
            for i, r in enumerate(self._board):
                orig = r.copy()
                new_row = self._slide_a_row(r[::-1])[::-1]
                if orig != new_row:
                    success = True
                    self._board[i] = new_row
        elif dir == Direction.UP:
            for c in range(len(self._board[0])):
                orig_col = []
                for r in range(len(self._board)):
                    orig_col.append(self._board[r][c])
                new_col = self._slide_a_row(orig_col)
                if orig_col != new_col:
                    success = True
                    i, r = 0, 0
                    while i < len(new_col) and r < len(self._board):
                        self._board[r][c] = new_col[i]
                        i += 1
                        r += 1
                    while r < len(self._board):
                        self._board[r][c] = None
                        r += 1
        elif dir == Direction.DOWN:
            for c in range(len(self._board[0])):
                orig_col = []
                for r in range(len(self._board)):
                    orig_col.append(self._board[r][c])
                new_col = self._slide_a_row(orig_col[::-1])[::-1]
                if orig_col != new_col:
                    success = True
                    i, r = 0, 0
                    while i < len(new_col) and r < len(self._board):
                        self._board[r][c] = new_col[i]
                        i += 1
                        r += 1
                    while r < len(self._board):
                        self._board[r][c] = None
                        r += 1
        return success

    def add_new_element(self):
        empty_cells = []
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if self._board[r][c] == None:
                    empty_cells.append((r,c))
        
        if not empty_cells:
            raise RuntimeError("No empty cell to add new numbers")

        i = random.randint(0, len(empty_cells)-1)
        r, c = empty_cells[i]
        self._board[r][c] = 2

    def get_max(self):
        curr_max = 2
        for r in self._board:
            for c in r:
                if c is not None and c > curr_max:
                    curr_max = c
        return curr_max

    @property
    def board(self):
        return self._board

    def _slide_a_row(self, row):
        prev = None
        output = []
        for c in row:
            if c is None:
                continue
            if prev is None:
                prev = c
                continue
            if prev == c:
                output.append(prev * 2)
                prev = None
            else:
                output.append(prev)
                prev = c
        if prev is not None:
            output.append(prev)
        return output + [None] * (len(row) - len(output))
 