# Evan Otero
#
# Maze Solver
#
# April 30, 2015
#

from Tkinter import *
import tkFileDialog
from time import sleep


def load():
    fname=tkFileDialog.askopenfilename(title='Select file',parent=window)
    displayname = fname
    p = displayname.rfind('/')
    if p>=0:
        displayname = displayname[p+1:]
    filename_entry.delete(0,END)
    filename_entry.insert(0,displayname)
    path_display.delete(1.0,END)
    get_maze(fname)


def get_maze(fname):
    global maze, rows, cols, startpos, exitpos
    f = open(fname,'r')
    line = f.readline()
    s = line.strip().split()
    rows,cols = int(s[0]),int(s[1])
    maze = [[0 for c in range(cols)] for r in range(rows)] 
    for i in range(rows):
        line = f.readline()
        s = line.strip().split()
        for j in range(len(s)):
            state = int(s[j])
            maze[i][j] = state
            if state==START:
                startpos = (i,j)
            if state==DEST:
                exitpos = (i,j)
    display_maze(maze)


def display_maze(maze):
    sqsize = min(MAXSQSIZE,MAXWIDTH/cols,MAXHEIGHT/rows)
    maze_display.config(width=cols*sqsize+2,height=rows*sqsize+2)
    for i in range(rows):
        for j in range(cols):
            rect = maze_display.create_rectangle(j*sqsize+1,i*sqsize+1,(j+1)*sqsize+1,(i+1)*sqsize+1,fill=colors[maze[i][j]],width=1)
            maze[i][j] = (rect,maze[i][j])


def reset():
    for i in range(rows):
        for j in range(cols):
            (rect, state) = maze[i][j]
            if state == VISITED:
                maze[i][j] = (rect, OPEN)
                maze_display.itemconfigure(rect,fill='white')
    (x, y) = exitpos
    (rect, state) = maze[x][y]
    maze_display.itemconfigure(rect,fill='red')
    (x, y) = startpos
    (rect, state) = maze[x][y]
    maze_display.itemconfigure(rect,fill='green')
    path_display.delete(1.0,END)
    window.update()


def find_path(pos,path):
    (x, y) = pos
    neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
    for n in neighbors:
        # print n  # DEBUG
        delay_time = timer_entry.get()

        (ix, jx) = n
        if x + ix >= 0 and x + ix <= rows-1:
            if y + jx >= 0 and y + jx <= cols-1:
                r = x + ix
                c = y + jx
                # print r, c  # DEBUG
                (rect, state) = maze[r][c]

                if state == DEST:
                    path.append((r,c))
                    return True
                elif state == OPEN:
                    maze[r][c] = (rect, VISITED)
                    maze_display.itemconfigure(rect,fill='gray')
                    if delay_time.isdigit():
                        # print delay_time  # DEBUG
                        delay_time = int(delay_time)
                        delay_time = delay_time/1000.0
                        sleep(delay_time)
                        window.update()
                    path.append((r,c))
                    recurse = find_path((r,c),path)
                    if recurse:
                        return True
                    else:
                        path.remove((r,c))
    return False


def solve():
    global path
    path = []
    path.append(startpos)
    if find_path(startpos, path):
        path_display.insert(1.0, path)
        for sq in path:
            (r, c) = sq
            maze_display.itemconfigure(maze[r][c][0],fill='yellow')
        window.update()
    else:
        path_display.insert(1.0, 'No path found!')

### Square States ###   
OPEN = 0
WALL = 1
START = 2
DEST = 3
VISITED = 4

### Square Colors ###
colors = ['white','black','green','red','gray']

### Size Limits ###
MAXSQSIZE=30
MAXWIDTH=800
MAXHEIGHT=560

### GUI ###
window = Tk()
window.title('Amazing Maze Solver')

button_bar = Frame(window)
button_bar.grid(row=0,column=0)

controls = Frame(button_bar)
controls.grid(row=0,column=0)

flabel = Label(controls,text='File:')
flabel.grid(row=0,column=0,sticky='E')
filename_entry = Entry(controls,width=30)
filename_entry.insert(0,'<no maze loaded>')
filename_entry.grid(row=0,column=1,sticky='W')

tlabel = Label(controls,text='Timer (ms):')
tlabel.grid(row=1,column=0,sticky='E')
timer_entry = Entry(controls,width=30)
timer_entry.insert(0,'20')
timer_entry.grid(row=1,column=1,sticky='W')

buttons1 = Frame(button_bar)
buttons1.grid(row=0,column=1)

load_button = Button(buttons1,text='load',command=load)
load_button.grid(row=0,column=0)
solve_button = Button(buttons1,text='solve',command=solve)
solve_button.grid(row=0,column=1)
reset_button = Button(buttons1,text='reset',command=reset)
reset_button.grid(row=0,column=2)

pane = Frame(window)
pane.grid(row=1,column=0)

maze_display = Canvas(pane,width=200,height=140,bd=0,highlightthickness=0,highlightbackground='black')
maze_display.grid(row=0,column=0)

scrollbar = Scrollbar(pane)
scrollbar.grid(row=1, column=1, sticky='NS')

path_display = Text(pane,width=80,height=5,bd=1,wrap=WORD, yscrollcommand=scrollbar.set)
path_display.grid(row=1,column=0,sticky='EW')

scrollbar.config(command=path_display.yview)

window.mainloop()
