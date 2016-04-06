python-fun
=============
This is a collection of Python files that have been used in class or were created for personal enjoyment.

Some of these projects were written when I first started learning to program (i.e. TicTacToe).  The workarounds used for situations where advanced concepts had not yet been introduced are interesting to read.

Standing Ovation
----------------
Everyone in the audience has a shyness level. An audience member with shyness level **S<sup>i</sup>** will wait until at least **S<sup>i</sup>** other audience members have already stood up to clap, and if so, she will immediately stand up and clap. If **S<sup>i</sup>** = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does.

##Input

The first line of the input gives the number of test cases, **T**. **T** test cases follow. Each consists of one line with **S<sup>max</sup>**, the maximum shyness level of the shyest person in the audience, followed by a string of **S<sup>max</sup> + 1** single digits. The **k**th digit of this string (counting starting from 0) represents how many people in the audience have shyness level **k**. For example, the string "409" would mean that there were four audience members with **S<sup>i</sup>** = 0 and nine audience members with **S<sup>i</sup>** = 2 (and none with **S<sup>i</sup>** = 1 or any other value). Note that there will initially always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.

##Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.

[Full problem can be found here](https://code.google.com/codejam/contest/6224486/dashboard)

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
