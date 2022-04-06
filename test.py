### print("kenny is a loser")

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
erase_button = ttk.Button(content, text = 'Erase')
### IR table button?

    ### button positions
z_inButton.grid(row=1, column=0)
z_outButton.grid(row=2, column=0)

erase_button.grid(row=4, column=0)

#top_frame = ttk.Labelframe(content, borderwidth=5, relief="ridge", width=1000, height=330, text='Known Spectra')
#top_frame.grid(column = 2, row =0, columnspan=3, rowspan=8)

### add image
    ### finds the file path
def open_image():
    global my_image
    root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
    ### opens the image
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    #my_image_label.grid(column=2, row=0)
    my_canvas.create_image(0,0, image=my_image)

### drawing function!!!!!!!!
def paint(event):
   python_green = "#476042"
   x1, y1 = (event.x - 1), (event.y - 1)
   x2, y2 = (event.x + 1), (event.y + 1)
   my_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

### for unknown spectra!
my_canvas = tkinter.Canvas(content, bg='white', height=330, width=1000)
my_canvas.grid(column=2, row=0, columnspan=3, rowspan=10)

### for known spectra!
sec_canvas = tkinter.Canvas(content, bg='white', height=330, width=1000)
sec_canvas.grid(column=2, row=11, columnspan=3, rowspan=10)

### figure out how to make this work AFTER you click the button
draw_button = ttk.Button(content, text = "Draw", command=my_canvas.bind( "<B1-Motion>", paint ))
draw_button.grid(row=3, column=0)

add_image = ttk.Button(content, text='Add Image', command=open_image)
add_image.grid(column=0, row=0)

root.mainloop()