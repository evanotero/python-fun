# Evan Otero
#
# This program runs the game Tic-Tac-Toe using tkinter
# to display the game board.
#
# Tic-Tac-Toe
# v. 2.0.0
#
#

from Tkinter import *


# def button(event):  # Tracks cursor position for Button-1
#     x, y = event.x, event.y
#     print('{}, {}'.format(x, y))


def drawGrid(w, h):  # The grid for a Tic-Tac-Toe board is drawn
    canvas.create_line((1/float(3))*w, 0, (1/float(3))*w, h)  # First Column Line
    canvas.create_line((2/float(3))*w, 0, (2/float(3))*w, h)  # Second Column Line
    canvas.create_line(0, (1/float(3))*h, w, (1/float(3))*h)  # First Row Line
    canvas.create_line(0, (2/float(3))*h, w, (2/float(3))*h)  # Second Row Line
    board.update()


def drawX(x1, y1, x2, y2):  # X is drawn in its respective grid
    canvas.create_line(x1, y1, x2, y2, fill='red')
    canvas.create_line(x2, y1, x1, y2, fill='red')
    board.update()


def drawO(x1, y1, x2, y2):  # O is drawn in its respective grid
    canvas.create_oval(x1, y1, x2, y2, width=1, outline='blue')
    board.update()


def turnLogic():
    global turn
    while xWins() != True and oWins() != True:
        x_Turn()
        if xWins() == True:
            print 'Tic-Tac-Toe, 3 in a row!  X Wins!'
            break
        elif turn == 9:
            print 'No winner!  You tied!'
            break
        o_Turn()
        if oWins() == True:
            print 'Tic-Tac-Toe, 3 in a row!  O Wins!'
            break
        elif turn == 9:
            print 'No winner!  You tied!'
            break
        if turn > 9:
            print '<Turn Error 1>'
    exit_input = raw_input('Press ENTER to close game: ')
    while exit_input != '':
        print 'That is not a recognized command!'
        exit_input = raw_input('Press ENTER to close game: ')
    quit()


def x_Turn():
    x_input = raw_input('X, Please enter a grid number: ')
    while x_input == '' or 0 > int(x_input) or int(x_input) > 9:
        print 'You did not enter an appropriate grid number.'
        print 'You must enter a number between 1 and 9.'
        x_input = raw_input('X, Please enter a grid number: ')
    x_gridInterpreter(int(x_input))


def o_Turn():
    o_input = raw_input('O, Please enter a grid number: ')
    while o_input == '' or 0 > int(o_input) or int(o_input) > 9:
        print 'You did not enter an appropriate grid number.'
        print 'You must enter a number between 1 and 9.'
        o_input = raw_input('O, Please enter a grid number: ')
    o_gridInterpreter(int(o_input))


def xWins():
    global block_1
    global block_2
    global block_3
    global block_4
    global block_5
    global block_6
    global block_7
    global block_8
    global block_9
    if block_1 == 1 and block_2 == 1 and block_3 == 1:
        return True
    elif block_4 == 1 and block_5 == 1 and block_6 == 1:
        return True
    elif block_7 == 1 and block_8 == 1 and block_9 == 1:
        return True
    elif block_1 == 1 and block_4 == 1 and block_7 == 1:
        return True
    elif block_2 == 1 and block_5 == 1 and block_8 == 1:
        return True
    elif block_3 == 1 and block_6 == 1 and block_9 == 1:
        return True
    elif block_1 == 1 and block_5 == 1 and block_9 == 1:
        return True
    elif block_3 == 1 and block_5 == 1 and block_7 == 1:
        return True
    else:
        return False


def oWins():
    global block_1
    global block_2
    global block_3
    global block_4
    global block_5
    global block_6
    global block_7
    global block_8
    global block_9
    if block_1 == 2 and block_2 == 2 and block_3 == 2:
        return True
    elif block_4 == 2 and block_5 == 2 and block_6 == 2:
        return True
    elif block_7 == 2 and block_8 == 2 and block_9 == 2:
        return True
    elif block_1 == 2 and block_4 == 2 and block_7 == 2:
        return True
    elif block_2 == 2 and block_5 == 2 and block_8 == 2:
        return True
    elif block_3 == 2 and block_6 == 2 and block_9 == 2:
        return True
    elif block_1 == 2 and block_5 == 2 and block_9 == 2:
        return True
    elif block_3 == 2 and block_5 == 2 and block_7 == 2:
        return True
    else:
        return False


def x_gridInterpreter(userInput):
    grid = userInput
    w = WIDTH
    h = HEIGHT
    if grid == 1:
        if block_1_(1):
            drawX(0, 0, (1/float(3))*w, (1/float(3))*h)
    elif grid == 2:
        if block_2_(1):
            drawX((1/float(3))*w, 0, (2/float(3))*w, (1/float(3))*h)
    elif grid == 3:
        if block_3_(1):
            drawX((2/float(3))*w, 0, w, (1/float(3))*h)
    elif grid == 4:
        if block_4_(1):
            drawX(0, (1/float(3))*h, (1/float(3))*w, (2/float(3))*h)
    elif grid == 5:
        if block_5_(1):
            drawX((1/float(3))*w, (1/float(3))*h, (2/float(3))*w, (2/float(3))*h)
    elif grid == 6:
        if block_6_(1):
            drawX((2/float(3))*w, (1/float(3))*h, w, (2/float(3))*h)
    elif grid == 7:
        if block_7_(1):
            drawX(0, (2/float(3))*h, (1/float(3))*w, h)
    elif grid == 8:
        if block_8_(1):
            drawX((1/float(3))*w, (2/float(3))*h, (2/float(3))*w, h)
    elif grid == 9:
        if block_9_(1):
            drawX((2/float(3))*w, (2/float(3))*h, w, h)
    else:
        print '<error x_gridInterpreter>'


def o_gridInterpreter(userInput):
    grid = userInput
    w = WIDTH
    h = HEIGHT
    if grid == 1:
        if block_1_(2):
            drawO(0, 0, (1/float(3))*w, (1/float(3))*h)
    elif grid == 2:
        if block_2_(2):
            drawO((1/float(3))*w, 0, (2/float(3))*w, (1/float(3))*h)
    elif grid == 3:
        if block_3_(2):
            drawO((2/float(3))*w, 0, w, (1/float(3))*h)
    elif grid == 4:
        if block_4_(2):
            drawO(0, (1/float(3))*h, (1/float(3))*w, (2/float(3))*h)
    elif grid == 5:
        if block_5_(2):
            drawO((1/float(3))*w, (1/float(3))*h, (2/float(3))*w, (2/float(3))*h)
    elif grid == 6:
        if block_6_(2):
            drawO((2/float(3))*w, (1/float(3))*h, w, (2/float(3))*h)
    elif grid == 7:
        if block_7_(2):
            drawO(0, (2/float(3))*h, (1/float(3))*w, h)
    elif grid == 8:
        if block_8_(2):
            drawO((1/float(3))*w, (2/float(3))*h, (2/float(3))*w, h)
    elif grid == 9:
        if block_9_(2):
            drawO((2/float(3))*w, (2/float(3))*h, w, h)
    else:
        print '<error o_gridInterpreter>'


###################################################################
"""
Block/Grid Ownership Logic
0 = no owner
1 = x
2 = o
"""


def block_1_(owner):
    global turn
    global block_1
    if block_1 == 0:  # If no owner
        if owner == 1:  # If x is the owner
            block_1 = 1  # Set the owner value to x
        elif owner == 2:   # If o is the owner
            block_1 = 2  # Set the owner value to o
        turn += 1  # This action counts as 1 turn
        return True  # The block had no previous owner and can contiue with the draw function
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()  # Re-do turn
        elif owner == 2:
            o_Turn()  # Re-do turn
        else:
            print '<unexpected error b1>'
        return False  # The block had a previous owner and cannot continue with the draw function


def block_2_(owner):
    global turn
    global block_2
    if block_2 == 0:
        if owner == 1:
            block_2 = 1
        elif owner == 2:
            block_2 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b2>'
        return False


def block_3_(owner):
    global turn
    global block_3
    if block_3 == 0:
        if owner == 1:
            block_3 = 1
        elif owner == 2:
            block_3 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b3>'
        return False


def block_4_(owner):
    global turn
    global block_4
    if block_4 == 0:
        if owner == 1:
            block_4 = 1
        elif owner == 2:
            block_4 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b4>'
        return False


def block_5_(owner):
    global turn
    global block_5
    if block_5 == 0:
        if owner == 1:
            block_5 = 1
        elif owner == 2:
            block_5 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b5>'
        return False


def block_6_(owner):
    global turn
    global block_6
    if block_6 == 0:
        if owner == 1:
            block_6 = 1
        elif owner == 2:
            block_6 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b6>'
        return False


def block_7_(owner):
    global turn
    global block_7
    if block_7 == 0:
        if owner == 1:
            block_7 = 1
        elif owner == 2:
            block_7 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b7>'
        return False


def block_8_(owner):
    global turn
    global block_8
    if block_8 == 0:
        if owner == 1:
            block_8 = 1
        elif owner == 2:
            block_8 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b8>'
        return False


def block_9_(owner):
    global turn
    global block_9
    if block_9 == 0:
        if owner == 1:
            block_9 = 1
        elif owner == 2:
            block_9 = 2
        turn += 1
        return True
    else:
        print 'This grid is already taken!'
        print 'You must enter an unoccupied grid.'
        if owner == 1:
            x_Turn()
        elif owner == 2:
            o_Turn()
        else:
            print '<unexpected error b9>'
        return False

##########################################################


block_1 = 0  # Block 1 Ownership Counter
block_2 = 0  # Block 2 Ownership Counter
block_3 = 0  # Block 3 Ownership Counter
block_4 = 0  # Block 4 Ownership Counter
block_5 = 0  # Block 5 Ownership Counter
block_6 = 0  # Block 6 Ownership Counter
block_7 = 0  # Block 7 Ownership Counter
block_8 = 0  # Block 8 Ownership Counter
block_9 = 0  # Block 9 Ownership Counter
turn = 0     # Turn Counter

WIDTH = 500
HEIGHT = 500

board = Tk()
board.title("Tic-Tac-Toe")
canvas = Canvas(board, width=WIDTH, height=HEIGHT, highlightthickness=0,
                bg='white')
canvas.grid(row=0, column=0)

drawGrid(WIDTH, HEIGHT)
turnLogic()

# board.bind('<Button-1', button)
board.mainloop()

'''
Known Bugs:
    1.

Grid Numbering System:
_______
|1|2|3|
|-----|
|4|5|6|
|-----|
|7|8|9|
-------
'''
