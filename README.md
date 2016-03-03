python-fun
=============
This is a collection of Python files that have been used in class or were created for personal enjoyment.

Some of these projects were written when I first started learning to program (i.e. TicTacToe).  The workarounds used for situations where advanced concepts had not yet been introduced are interesting to read.

Maze Solver
------------
Finds a path in a maze using recursive backtracking.  The format to represent a maze in a text file is
the following:
- The first line of the file contains two integrs (# of rows [R] and # of columns [C]).
- The rest of the file will be R rows of C integers.  The values of the integers will be:
  - 0 = an empty space; 1 = a wall; 2 = the start; 3 = the exist

Markov
------
An order N Markov model is built from a piece of input text.  A segment of text is then generated
from the model.  Sample input texts have been provided.  This program uses Tkinter.

TicTacToe
-----
My first Python game written using basic knowledge of the langauge.  The game board is displayed
using Tkinter and input is read in through the console.  For the input, in order to choose the grid
you would like to play, use the following number system:
   
    -------------
    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |
    -------------

Divisor Generator
-----------------
This script generates a list of divisors for n.  Calculating all divisors of 100000000 took 00.000163s
(using datetime module).
