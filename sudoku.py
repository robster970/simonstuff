# ---------------------------------------------------------------
# Suduko solver - takes input and calculates solution (easy
#   puzzles only
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Initialise libraries, functions and classes
# ---------------------------------------------------------------


import numpy as np


def midstr(s, c):
    return s[c:c + 1]


class Cell:

    def __init__(self, startvalue, endvalue, possiblevalues):
        self.startvalue = startvalue
        self.endvalue = endvalue
        self.possiblevalues = possiblevalues


grid = np.empty((9, 9), dtype=object)


# ---------------------------------------------------------------
# Load grid - this should be a UI in which values can be type.
#   Coud be entered as series of values, values/grid position etc
#   eg rowOfValues = raw_input('Enter row %b' % row_no
#   But in this case loaded from strings
# ---------------------------------------------------------------


def loadgrid():
    for row in range(9):  # load arrays with cell objects

        for col in range(9):
            grid[row, col] = Cell(0, 0, 0)

    for col in range(9):  # for each col, load each row with corresponding test data
        grid[0, col].startvalue = int(midstr('034567890', col))
        grid[1, col].startvalue = int(midstr('001002003', col))
        grid[2, col].startvalue = int(midstr('002002003', col))
        grid[3, col].startvalue = int(midstr('003002003', col))
        grid[4, col].startvalue = int(midstr('004002003', col))
        grid[5, col].startvalue = int(midstr('005002004', col))
        grid[6, col].startvalue = int(midstr('001602003', col))
        grid[7, col].startvalue = int(midstr('001072003', col))
        grid[8, col].startvalue = int(midstr('001008003', col))

    for row in range(9):  # preset final values to initial values (0 = not known)

        for col in range(9):
            grid[row, col].endvalue = grid[row, col].startvalue

            #print(row, col, grid[row, col].startvalue)


# ---------------------------------------------------------------
# Print grid - this should be a UI in which values are displayed
# ---------------------------------------------------------------

def printgrid():
    for row in range(9):

        for col in range(9):
            print(row, col, grid[row, col].startvalue, grid[row, col].endvalue, grid[row, col].possiblevalues)


# ---------------------------------------------------------------
# Main processing - initialise grid, run solver and display
#   resultsInitialise libraries, functions and classes
# ---------------------------------------------------------------


loadgrid()  # loads the Sudoku grid with initial values
solved = False

# while not solved:
#  iterates solving the grid (using simple method) until solved
#    solveGrid()

printgrid()  # prints the final answer

exit()
