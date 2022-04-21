from ctypes import resize
from email.mime import image
from fileinput import filename
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import ImageTk, Image
from tkinter import filedialog as fd

### creates the program
root = Tk()  ### naming the variable and creates a Tk class
root.title('Eye-tracking Study Interface')

### sizing the window
screen_height = root.winfo_screenheight()
h = screen_height
#print(screen_height)
screen_width = root.winfo_screenwidth()
w = screen_width
#print(screen_width)
x=(w-200)/2
y=(330)/2


### makes this full screen
root.geometry("%dx%d" % (screen_width, screen_height))
root.resizable(False, False)

### setups of the drawing feature so that the button is OFF initially
is_draw_enable = FALSE

is_erase_enable = FALSE

### widgets!
content = ttk.Frame(root)
content.grid(column = 0, row = 0)



### opening the IR/MS layout
def IR_MS_open():
    ### ALL FUNCTIONS
    ### opening a file on the top canvas
    def open_topimage():
        global my_image, img, curr_width, curr_height, og_img, image1
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        img = Image.open(root.filename)
        og_img = Image.open(root.filename)
        ### default scale value...
        resize_ratio = 1

        ### image dimenisions check for scaling...
        if img.height > (330):
            resize_ratio = (img.height/(330))
        else:
            if img.width > (root.winfo_screenwidth() - 200):
                resize_ratio = (img.width/(root.winfo_screenwidth() - 200))

        ### resize image...
        curr_width = int(img.width/resize_ratio)
        curr_height = int(img.height/resize_ratio)
        img = img.resize((curr_width,curr_height), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)

        my_image_label = Label(image=my_image)
        #my_image_label.grid(column=2, row=0)
        ### create image at center of canvas...
        image1 = my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

    ### adds image to the bottom canvas
    def open_bottomimage():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        sec_img = Image.open(root.filename)
        ogsec_img = Image.open(root.filename)
        ### default scale value...
        resize_ratio = 1

        ### image dimenisions check for scaling...
        if sec_img.height > (330):
            resize_ratio = (sec_img.height/(330))
        else:
            if sec_img.width > (root.winfo_screenwidth() - 200):
                resize_ratio = (sec_img.width/(root.winfo_screenwidth() - 200))

        ### resize image...
        curr_width2 = int(sec_img.width/resize_ratio)
        curr_height2 = int(sec_img.height/resize_ratio)
        sec_img = sec_img.resize((curr_width2, curr_height2), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)

        my_secimage_label = Label(image=my_secimage)
        #my_image_label.grid(column=2, row=0)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### This function works but it loses resolution and is generally bad...
    def zoom():
        global my_image, img, curr_width, curr_height, og_img
        curr_width = curr_width*2
        curr_height = curr_height*2
        img = og_img.resize((int(curr_width), int(curr_height)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

    # bottom canvas
    def zoom2():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        curr_width2 = curr_width2*2
        curr_height2 = curr_height2*2
        sec_img = ogsec_img.resize((int(curr_width2), int(curr_height2)), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### zoom out?
    def zoom_out():
        global my_image, img, curr_width, curr_height, og_img
        curr_width = curr_width/2
        curr_height = curr_height/2
        img = og_img.resize((int(curr_width), int(curr_height)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

    def zoom_out2():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        curr_width2 = curr_width2/2
        curr_height2 = curr_height2/2
        sec_img = ogsec_img.resize((int(curr_width2), int(curr_height2)), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### drawing function
    def paint(event):
        global drawing
        if is_draw_enable == TRUE:
            python_green = "#476042"
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            drawing = my_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    ### for bottom canvas too
    ### drawing function (do we need two drawing features???????????)
    def paint2(event):
        if is_draw_enable == TRUE:
            python_green = "#476042"
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            sec_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    ### turns the drawing feature on and off
    def toggle_draw():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            my_canvas.bind("<B1-Motion>", paint)
            sec_canvas.bind("<B1-Motion>", paint)
        else:
            is_draw_enable = FALSE

    ### for bottom canvas too
    def toggle_draw2():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            sec_canvas.bind("<B1-Motion>", paint2)
        else:
            is_draw_enable = FALSE

    ### erase feature
    def erase():
        global drawing
        if is_erase_enable == TRUE:
            my_canvas.delete(drawing)

    def toggle_erase():
        global is_erase_enable
        if is_erase_enable == FALSE:
            is_erase_enable = TRUE
            erase
        else:
            is_erase_enable = FALSE

    ### IR table
    def open_IR():
        IR_root = Tk()  ### naming the variable and creates a Tk class
        IR_root.title('IR Table')
        IR_canvas = Canvas(IR_root)
        IR_img = PhotoImage(file="IRtable.jpg")
        IR_canvas.create_image(image=IR_img)
        IR_root.mainloop()



    def left(event):
        global image1
        x = -20
        y = 0
        my_canvas.move(image1, x, y)

    def right(event):
        global image1
        x = 20
        y = 0
        my_canvas.move(image1, x, y)

    def up(event):
        x = 0
        y = -20
        my_canvas.move(image1, x, y)

    def down(event):
        x = 0
        y = 20
        my_canvas.move(image1, x, y)


    # Bind the move function
    content.bind("<Left>", left)
    content.bind("<Right>", right)
    content.bind("<Up>", up)
    content.bind("<Down>", down)




        ### editing options buttons and their positions
    ### figure out how to turn it back on
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw)
    draw_button.grid(row=3, column=0)

    # for bottom canvas
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw2)
    draw_button.grid(row=14, column=0)
    ### IR table
    IR_button = ttk.Button(content, text = 'IR Table', command=open_IR)
    IR_button.grid(row=16, column=0)

    # zoom for the top canvas
    z_inButton = ttk.Button(content, text="Zoom In", command=zoom)
    z_inButton.grid(row=1, column=0)
    z_outButton = ttk.Button(content, text="Zoom Out", command=zoom_out)
    z_outButton.grid(row=2, column=0)

    # zoom for the bottom canvas
    z_inButton = ttk.Button(content, text="Zoom In", command=zoom2)
    z_inButton.grid(row=12, column=0)
    z_outButton = ttk.Button(content, text="Zoom Out", command=zoom_out2)
    z_outButton.grid(row=13, column=0)

    # erase for top canvas
    erase_button = ttk.Button(content, text = 'Erase', command=toggle_erase)
    erase_button.grid(row=4, column=0)

    # erase for bottom canvas
    erase_button = ttk.Button(content, text = 'Erase')
    erase_button.grid(row=15, column=0)
    ### IR table button?

    ### to add an image into the top canvas :)
    add_image = ttk.Button(content, text='Add Image', command=open_topimage)
    add_image.grid(column=0, row=0)

    ### adds image to the bottom canvas
    add_image = ttk.Button(content, text='Add Image', command=open_bottomimage)
    add_image.grid(column=0, row=11)

    ### CANVASES
    ### for unknown spectra!
    my_canvas = tkinter.Canvas(content, height=330, width=(root.winfo_screenwidth() - 200))
    my_canvas.grid(column=2, row=0, columnspan=3, rowspan=10)

    ### for known spectra!
    sec_canvas = tkinter.Canvas(content, height=330, width=(root.winfo_screenwidth() - 200))
    sec_canvas.grid(column=2, row=11, columnspan=3, rowspan=10)







### opening fingerprint layout
def fingerprint_open():
    ### ALL FUNCTIONS
    ### opening a file on the top canvas
    def open_leftimage():
        global my_image, img, curr_width, curr_height, og_img, image1
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        img = Image.open(root.filename)
        og_img = Image.open(root.filename)
        ### default scale value...
        resize_ratio = 1

        ### image dimenisions check for scaling...
        if img.height > (640):
            resize_ratio = (img.height/(640))
        else:
            if img.width > (600):
                resize_ratio = (img.width/(600))

        ### resize image...
        curr_width = int(img.width/resize_ratio)
        curr_height = int(img.height/resize_ratio)
        img = img.resize((curr_width,curr_height), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)

        my_image_label = Label(image=my_image)
        ### create image at center of canvas...
        image1 = my_canvas.create_image((600/2),(640/2), image=my_image)

    ### adds image to the bottom canvas
    def open_bottomimage():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        sec_img = Image.open(root.filename)
        ogsec_img = Image.open(root.filename)
        ### default scale value...
        resize_ratio = 1

        ### image dimenisions check for scaling...
        if sec_img.height > (330):
            resize_ratio = (sec_img.height/(330))
        else:
            if sec_img.width > (root.winfo_screenwidth() - 200):
                resize_ratio = (sec_img.width/(root.winfo_screenwidth() - 200))

        ### resize image...
        curr_width2 = int(sec_img.width/resize_ratio)
        curr_height2 = int(sec_img.height/resize_ratio)
        sec_img = sec_img.resize((curr_width2, curr_height2), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)

        my_secimage_label = Label(image=my_secimage)
        #my_image_label.grid(column=2, row=0)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### This function works but it loses resolution and is generally bad...
    def zoom():
        global my_image, img, curr_width, curr_height, og_img
        curr_width = curr_width*2
        curr_height = curr_height*2
        img = og_img.resize((int(curr_width), int(curr_height)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

    # bottom canvas
    def zoom2():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        curr_width2 = curr_width2*2
        curr_height2 = curr_height2*2
        sec_img = ogsec_img.resize((int(curr_width2), int(curr_height2)), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### zoom out?
    def zoom_out():
        global my_image, img, curr_width, curr_height, og_img
        curr_width = curr_width/2
        curr_height = curr_height/2
        img = og_img.resize((int(curr_width), int(curr_height)), Image.ANTIALIAS)
        my_image = ImageTk.PhotoImage(img)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_image)

    def zoom_out2():
        global my_secimage, sec_img, curr_width2, curr_height2, ogsec_img
        curr_width2 = curr_width2/2
        curr_height2 = curr_height2/2
        sec_img = ogsec_img.resize((int(curr_width2), int(curr_height2)), Image.ANTIALIAS)
        my_secimage = ImageTk.PhotoImage(sec_img)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=my_secimage)

    ### drawing function
    def paint(event):
        global drawing
        if is_draw_enable == TRUE:
            python_green = "#476042"
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            drawing = my_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    ### for bottom canvas too
    ### drawing function (do we need two drawing features???????????)
    def paint2(event):
        if is_draw_enable == TRUE:
            python_green = "#476042"
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            sec_canvas.create_oval(x1, y1, x2, y2, fill=python_green)

    ### turns the drawing feature on and off
    def toggle_draw():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            my_canvas.bind("<B1-Motion>", paint)
            sec_canvas.bind("<B1-Motion>", paint)
        else:
            is_draw_enable = FALSE

    ### for bottom canvas too
    def toggle_draw2():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            sec_canvas.bind("<B1-Motion>", paint2)
        else:
            is_draw_enable = FALSE

    ### erase feature
    def erase():
        global drawing
        if is_erase_enable == TRUE:
            my_canvas.delete(drawing)

    def toggle_erase():
        global is_erase_enable
        if is_erase_enable == FALSE:
            is_erase_enable = TRUE
            erase
        else:
            is_erase_enable = FALSE

    ### IR table
    def open_IR():
        IR_root = Tk()  ### naming the variable and creates a Tk class
        IR_root.title('IR Table')
        IR_canvas = Canvas(IR_root)
        IR_img = PhotoImage(file="IRtable.jpg")
        IR_canvas.create_image(image=IR_img)
        IR_root.mainloop()



    def left(event):
        global image1
        x = -20
        y = 0
        my_canvas.move(image1, x, y)

    def right(event):
        global image1
        x = 20
        y = 0
        my_canvas.move(image1, x, y)

    def up(event):
        x = 0
        y = -20
        my_canvas.move(image1, x, y)

    def down(event):
        x = 0
        y = 20
        my_canvas.move(image1, x, y)


    # Bind the move function
    content.bind("<Left>", left)
    content.bind("<Right>", right)
    content.bind("<Up>", up)
    content.bind("<Down>", down)




        ### editing options buttons and their positions
    ### figure out how to turn it back on
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw)
    draw_button.grid(row=10, column=1)

    # for bottom canvas
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw2)
    draw_button.grid(row=10, column=3)

    # zoom for the top canvas
    z_inButton = ttk.Button(content, text="Zoom In", command=zoom)
    z_inButton.grid(row=10, column=2)
    z_outButton = ttk.Button(content, text="Zoom Out", command=zoom_out)
    z_outButton.grid(row=10, column=3)

    # zoom for the bottom canvas
    z_inButton = ttk.Button(content, text="Zoom In", command=zoom2)
    z_inButton.grid(row=10, column=7)
    z_outButton = ttk.Button(content, text="Zoom Out", command=zoom_out2)
    z_outButton.grid(row=10, column=8)

    # erase for top canvas
    erase_button = ttk.Button(content, text = 'Erase', command=toggle_erase)
    erase_button.grid(row=10, column=4)

    # erase for bottom canvas
    erase_button = ttk.Button(content, text = 'Erase')
    erase_button.grid(row=10, column=9)
    ### IR table button?

    ### to add an image into the top canvas :)
    add_image = ttk.Button(content, text='Add Image', command=open_leftimage)
    add_image.grid(column=1, row=10)

    ### adds image to the bottom canvas
    add_image = ttk.Button(content, text='Add Image', command=open_bottomimage)
    add_image.grid(column=6, row=10)

    ### CANVASES
    ### for unknown spectra!
    my_canvas = tkinter.Canvas(content, background='white', height=640, width=600)
    my_canvas.grid(column=1, row=0, columnspan=4, rowspan=10)

    ### for known spectra!
    sec_canvas = tkinter.Canvas(content, background='white',height=640, width=600)
    sec_canvas.grid(column=6, row=0, columnspan=4, rowspan=10)


### creating a menu
menubar = Menu(root, background='dark grey', foreground='black', activebackground='dark grey', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)

sub_menu = Menu(file, tearoff=0)
sub_menu.add_command(label='IR/MS', command=IR_MS_open)
sub_menu.add_command(label='Fingerprints', command=fingerprint_open)

file.add_cascade(label='New', menu=sub_menu)
file.add_command(label='Save')


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