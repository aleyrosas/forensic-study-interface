from ctypes import resize
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

### setups of the drawing feature so that the button is OFF initially
is_draw_enable = FALSE




### ALL FUNCTIONS!
### opening a file on the top canvas
def open_topimage():
    global my_image
    root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    #my_image_label.grid(column=2, row=0)
    my_canvas.create_image(0,0, image=my_image)

### adds image to the bottom canvas
def open_bottomimage():
    global my_secimage
    root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
    my_secimage = ImageTk.PhotoImage(Image.open(root.filename))
    my_secimage_label = Label(image=my_secimage)
    #my_image_label.grid(column=2, row=0)
    sec_canvas.create_image(0,0, image=my_secimage)

### drawing function!!!!!!!!
def paint(event):
    if is_draw_enable == TRUE:
        python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        my_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

### turns the drawing feature on and off
def toggle_draw():
    global is_draw_enable
    if is_draw_enable == FALSE:
        is_draw_enable = TRUE
        my_canvas.bind("<B1-Motion>", paint)
    else:
        is_draw_enable = FALSE




### widgets!
content = ttk.Frame(root)
content.grid(column = 0, row = 0)

    ### editing options buttons and their positions
### figure out how to turn it back on
draw_button = ttk.Button(content, text = "Draw", command=toggle_draw)
draw_button.grid(row=3, column=0)
z_inButton = ttk.Button(content, text="Zoom In")
z_inButton.grid(row=1, column=0)
z_outButton = ttk.Button(content, text="Zoom Out")
z_outButton.grid(row=2, column=0)
erase_button = ttk.Button(content, text = 'Erase')
erase_button.grid(row=4, column=0)
### IR table button?




### creating a menu
menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)
file.add_command(label='New')
file.add_command(label='Save')


### to add an image into the top canvas :)
add_image = ttk.Button(content, text='Add Image', command=open_topimage)
add_image.grid(column=0, row=0)

### adds image to the bottom canvas
add_image = ttk.Button(content, text='Add Image', command=open_bottomimage)
add_image.grid(column=0, row=11)

file.add_command(label='Open', command=open_topimage)
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





### CANVASES
### for unknown spectra!
my_canvas = tkinter.Canvas(content, bg='white', height=330, width=1000)
my_canvas.grid(column=2, row=0, columnspan=3, rowspan=10)

### for known spectra!
sec_canvas = tkinter.Canvas(content, bg='white', height=330, width=1000)
sec_canvas.grid(column=2, row=11, columnspan=3, rowspan=10)


root.mainloop()  ### displays everything until the program is closed!