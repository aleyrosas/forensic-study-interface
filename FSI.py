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
root.resizable(False, False)

### setups of the drawing feature so that the button is OFF initially
is_draw_enable = FALSE




### ALL FUNCTIONS!
### opening a file on the top canvas
def open_topimage():
    global my_image
    global img
    root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
    img = Image.open(root.filename)
    ### default scale value...
    resize_ratio = 1

    ### image dimenisions check for scaling...
    if img.height > (330):
        resize_ratio = (img.height/(330))
    else:
        if img.width > (root.winfo_screenwidth() - 200):
            resize_ratio = (img.width/(root.winfo_screenwidth() - 200))

    ### resize image...
    img = img.resize((int(img.width/resize_ratio),int(img.height/resize_ratio)), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(img)

    my_image_label = Label(image=my_image)
    #my_image_label.grid(column=2, row=0)
    ### create image at center of canvas...
    my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

### adds image to the bottom canvas
def open_bottomimage():
    global my_secimage
    global sec_img
    root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
    sec_img = Image.open(root.filename)
    ### default scale value...
    resize_ratio = 1

    ### image dimenisions check for scaling...
    if sec_img.height > (330):
        resize_ratio = (sec_img.height/(330))
    else:
        if sec_img.width > (root.winfo_screenwidth() - 200):
            resize_ratio = (sec_img.width/(root.winfo_screenwidth() - 200))

    ### resize image...
    sec_img = sec_img.resize((int(sec_img.width/resize_ratio),int(sec_img.height/resize_ratio)), Image.ANTIALIAS)
    my_secimage = ImageTk.PhotoImage(sec_img)

    my_secimage_label = Label(image=my_secimage)
    #my_image_label.grid(column=2, row=0)
    sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

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

### This function works but it loses resolution and is generally bad...
def zoom():
    global my_image
    global img
    img = img.resize((int(img.width * 2), int(img.height*2)), Image.ANTIALIAS)
    my_image = ImageTk.PhotoImage(img)
    my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)



### widgets!
content = ttk.Frame(root)
content.grid(column = 0, row = 0)

    ### editing options buttons and their positions
### figure out how to turn it back on
draw_button = ttk.Button(content, text = "Draw", command=toggle_draw)
draw_button.grid(row=3, column=0)
z_inButton = ttk.Button(content, text="Zoom In", command=zoom)
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
my_canvas = tkinter.Canvas(content, bg='white', height=330, width=(root.winfo_screenwidth() - 200))
my_canvas.grid(column=2, row=0, columnspan=3, rowspan=10)

### for known spectra!
sec_canvas = tkinter.Canvas(content, bg='white', height=330, width=(root.winfo_screenwidth() - 200))
sec_canvas.grid(column=2, row=11, columnspan=3, rowspan=10)


root.mainloop()  ### displays everything until the program is closed!