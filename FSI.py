from tkinter import *
from tkinter import ttk
### from PIL import ImageTk, Image
from tkinter.filedialog import *

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
top_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=1000, height=360)
top_frame.grid(column = 2, row = 0, columnspan=3, rowspan=8)

bottom_frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=1000, height=360)
bottom_frame.grid(column = 2, row=9, columnspan=3, rowspan=8)

    ### frames for additional spectra
ir_spec1 = ttk.Frame(content, borderwidth=5, relief='ridge', width=170, height=120)
ir_spec1.grid(column=9, row=0, rowspan=3)

def open_file():
    file = askopenfile(mode ='r', filetypes =[('Images', '*.jpg')])
    if file is not None:
        content = file.read()
        print(content)

### creating a menu? 
menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Save')

### idk how to make it open the files #####
### file.add_command(label='Open', Button(menubar, command=open_file()))
### file.add_command(label='Exit')
### menubar.add_cascade(label='File', menu=file)


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