from cgitb import text
from ctypes import resize
from fileinput import filename
from itertools import count
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import ImageTk, Image
from tkinter import filedialog as fd

### creates the program
root = Tk()  ### naming the variable and creates a Tk class
root.title('Eye-tracking Study Interface')

### sizing the window
screen_height = root.winfo_screenheight()
#print(screen_height)
screen_width = root.winfo_screenwidth()
#print(screen_width)

### makes this full screen
root.geometry("%dx%d" % (screen_width, screen_height))
root.resizable(screen_width, screen_height)

### widgets!
content = ttk.Frame(root)
content.grid(column = 0, row = 0)

#### goal to make a counter that keeps track of the zoom in and out factors that need to be
### applied to the original image
inital_count = 0
toggle_count = FALSE
x = 0

def clicker():
    global inital_count
    global new_count
    counter = inital_count
    x =+ 1
    if (counter < x): 
        print(counter)
        counter = x
        new_count = counter
        print(new_count)

def toggle_counter():
    global toggle_count
    if toggle_count == FALSE:
        toggle_count = TRUE
        clicker()
        print(new_count)
    toggle_count = FALSE
    print('this works!')


clicker_button = ttk.Button(content, text="test", command=toggle_counter)
clicker_button.pack()


root.mainloop()  ### displays everything until the program is closed!