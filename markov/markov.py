# Evan Otero
#
# April 14, 2015
#
# Markov model text generation
#

import os
from random import randint
from Tkinter import *


def create_action():
    global model
    global N
    global s

    N = order_entry.get()

    if N.isdigit():
        display_message('')

        filename = file_entry.get()
        if os.path.isfile(filename):
            display_message('')

            f = open(filename)
            s = f.read()
            model = dict()
            for x in range(len(s)-int(N)):
                successor_list = []
                seq = s[x:x+int(N)]
                successor_list = model.get(seq,[])
                next_char = s[x+int(N)]
                successor_list.append(next_char)
                model[seq] = successor_list
            #print model  # DEBUG dictionary
            
            gen_button.config(state=NORMAL)
        else:
            display_message('The file specified is not a file in the file system.')
    else:
        display_message('The order of the model is not a positive integer.')



def generate_action():
    M = 1000 # Size of Sample Generated

    output_string = s[:int(N)]

    for i in range(M):
        last_N_chars = output_string[len(output_string)-int(N):]
        if last_N_chars not in model:
            break
        possible_chars = model[last_N_chars]
        rand_index = randint(0,len(possible_chars)-1)
        char = possible_chars[rand_index]
        output_string += char

    output.delete(1.0, END)
    output.insert(1.0, output_string)


def display_message(message):
    message_label.config(text=message)   

window = Tk()
window.title('Markov model text generator')

output = Text(window,wrap=WORD,bd=10,highlightcolor='#a44245',highlightbackground='#a44245',highlightthickness=10,padx=5,pady=5)
output.grid(row=0,column=0,columnspan=2)

# create the entry widgets
order_label = Label(window,text='Enter the order of the model:')
order_label.grid(row=1,column=0,sticky='E')

order_entry = Entry(window)
order_entry.grid(row=1,column=1,sticky='W')

file_label = Label(window,text='Enter the name of the sample file:')
file_label.grid(row=2,column=0,sticky='E')

file_entry = Entry(window)
file_entry.grid(row=2,column=1,sticky='W')

message_label = Label(window,fg='red')
message_label.grid(row=3,column=0,columnspan=2)

# create buttons
create_button = Button(window,text='Create model',command=create_action)
create_button.grid(row=4,column=0,)

gen_button = Button(window,text='Generate text',command=generate_action)
gen_button.grid(row=4,column=1)
gen_button['state'] = DISABLED

window.mainloop()

