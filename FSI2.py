from cgitb import text
from fileinput import filename
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import fillcolor
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

known_canvas = tkinter.Canvas(root, bg='white', height=640, width=1000, name='known spectra')
known_canvas.grid(column=2, row=0, columnspan=3, rowspan=8)

### add image
    ### finds the file path
root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image)
my_image_label.grid(column=2, row=0)

known_canvas.create_image(my_image, fillcolor)




### creating a menu? 
menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Save')

### the command opens a file opening menu, but idk how to get it to put the image in the frame
#def open_file():
 #   global img
  #  filename = fd.askopenfile(mode='r', type="*.png")
   # img = open(filename)
    #image_frame = ttk.Labelframe(content, image=img, text = 'Image')
    #image_frame.grid(column=2, row=0)


file.add_command(label='Open')
file.add_command(label='Exit', command=root.quit)
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