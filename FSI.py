from fileinput import filename
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
    ### editing options buttons
z_inButton = ttk.Button(content, text="Zoom In")
z_outButton = ttk.Button(content, text="Zoom Out")
draw_button = ttk.Button(content, text = "Draw")
erase_button = ttk.Button(content, text = 'Erase')
### IR table button?

    ### button positions
z_inButton.grid(row=0, column=0)
z_outButton.grid(row=1, column=0)
draw_button.grid(row=2, column=0)
erase_button.grid(row=3, column=0)

    ### frames where I want the IR images to go
top_frame = ttk.Labelframe(content, borderwidth=5, relief="ridge", width=1000, height=330, text='Known Spectra')
top_frame.grid(column = 2, row =0, columnspan=3, rowspan=8)

bottom_frame = ttk.Labelframe(content, borderwidth=5, relief="ridge", width=1000, height=330, text='Unknown Spectra') #360)
bottom_frame.grid(column = 2, row=8, columnspan=3, rowspan=8)

    ### frames for additional spectra
ir_spec1 = ttk.Labelframe(content, borderwidth=5, relief='ridge', width=170, height=120, text='More')
ir_spec1.grid(column=9, row=0, rowspan=3)

### creating a menu? 
menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Save')

### the command opens a file opening menu, but idk how to get it to put the image in the frame
file.add_command(label='Open', command= fd.askopenfile(mode='r', type="*"))
file.add_command(label='Exit')
menubar.add_cascade(label='File', menu=file)


### edit menu options
edit = Menu(menubar, tearoff=0)
edit.add_command(label='Insert')
edit.add_command(label='Reorganize')
edit.add_command(label='Layout')
menubar.add_cascade(label='Edit', menu=edit)

### presentation option
present = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Present', menu=present)

root.config(menu=menubar)

root.mainloop()  ### displays everything until the program is closed!