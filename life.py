"""
    Pr2
    Natalie Brooks
    rosbrooks
"""

import os

class Life:
    """
    A class to implement Conway's Game of Life
    The game board is represented internally as a list of rows,
    each row itself being a list of Booleans (True == alive)
    """

    def __init__(self, height, width, initial_living):
        self.height = height
        self.width = width
        self.living = initial_living
        self.board = []
        self.generation = 0
        self.board_update()

    def board_update(self):
        """ Updates board of True / False lists """
        self.board = [[False for cols in range(self.width)] for rows in range(self.height)] # creates board of dead cells
        for cell in self.living:
            self.board[cell[0] - 1][cell[1] - 1] = True # changes live cells to True

    def __call__(self):
        """ Updates object when Life() is called """
        alive = []
        for y in range(self.height): # iterates through row values
            for x in range(self.width): # iterates through column values
                neighbors = self._next_to(y, x)
                if (y, x) in self.living:
                    if 2 <= neighbors <= 3:
                        alive.append((y, x))
                elif neighbors == 3:
                    alive.append((y, x))
        self.living = alive # updates self.living
        self.generation += 1
        self.board_update() # updates self.board

    def alive(self):
        """ Return a list of (y, x) tuples of current living cells """
        return self.living

    def _next_to(self, y, x):
        """ Returns number of cells
        next to selected cell. """
        neighbors = 0
        for column in range(y - 1, y + 2):
            for row in range(x - 1, x + 2):
                a = (column + self.height) % self.height
                b = (row + self.width) % self.width
                if (a, b) in self.living and (a, b) != (y, x):
                    neighbors += 1
        return neighbors

    def __str__(self):
        """ Returns string representation of board
        based on True / False list """
        main_string = ''
        row = 0
        while row < self.height: # iterates through rows
            row_string = ''
            column = 0
            while column < self.width: # iterates through columns
                if self.board[row - 1][column - 1] == True:
                    row_string += '#' # if cell is live, adds '#' to string
                else:
                    row_string += '.' # if cell is dead, adds '.' to string
                column += 1
            row_string += os.linesep # adds line separation at the end of each row
            main_string += row_string
            row += 1
        return main_string

    def show(self):
        """ Print the current state of the board on screen """
        print(self.__str__())

    def unshow(self):
        """ Clear the screen """
        os.system('cls' if os.name == 'nt' else 'clear')

