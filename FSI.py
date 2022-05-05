from ctypes import resize
from email.mime import image
from fileinput import filename
from msilib.schema import Directory
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import ImageTk, Image, ImageDraw
from tkinter import filedialog as fd
import os
from functools import partial
import turtle
from setuptools import Command



### used to keep track of all the other images, 
global init_imageobj
init_imageobj = []


#print(os.path)
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


### makes this full screen
root.geometry("%dx%d" % (screen_width, screen_height))
root.resizable(False, False)

### setups of the drawing feature so that the button is OFF initially
is_draw_enable = FALSE

is_erase_enable = FALSE

### widgets!
content = ttk.Frame(root)
content.grid(column = 0, row = 0)

class ImageOBJ:
    ### keeping track of all the image versions for all the functions
    ### pil is used to put the image on the canvas
    def __init__(self, filename):
        self.name = filename
        self.orignal = Image.open(self.name)
        self.thumbnail = Image.open(self.name).resize((100,100), Image.ANTIALIAS)
        self.pilThumbnail = ImageTk.PhotoImage(self.thumbnail)
        self.pilOrignal = ImageTk.PhotoImage(self.orignal)
        self.currVersion = Image.open(self.name)
        self.pilcurrVersion = ImageTk.PhotoImage(self.currVersion)
        ### going to be used for an undo feature
        self.imageStates = []
        self.imageStates.append(self.pilOrignal)
        ### transparent layer to draw on
        self.drawingCanvas = Image.new("RGBA", (self.currVersion.width, self.currVersion.height))
    
    ### resize the image and transparent layer
    def ImageScale(self, scale):
        ### for undo
        self.imageStates.append(self.currVersion)
        self.currVersion = self.orignal.resize((int(self.currVersion.width*scale), int(self.currVersion.height*scale)))
        ### resizing the drawing canvas
        self.drawingCanvas = self.drawingCanvas.resize((self.currVersion.width, self.currVersion.height), Image.ANTIALIAS)
        ### converting the image a format that supports transparency, just in case for merging
        temp = self.currVersion.convert("RGBA")
        ### puts drawing on canvas
        temp.paste(self.drawingCanvas, (0,0), self.drawingCanvas)
        self.pilcurrVersion = ImageTk.PhotoImage(temp)
    
    ### need to update the image everytime we make a change, UPDATING PIL image
    def update(self):
        self.drawingCanvas = self.drawingCanvas.resize((self.currVersion.width, self.currVersion.height), Image.ANTIALIAS)
        temp = self.currVersion.convert("RGBA")
        ### puts the drawing onto the image
        temp.paste(self.drawingCanvas, (0,0), self.drawingCanvas)
        self.pilcurrVersion = ImageTk.PhotoImage(temp)


### load in images for the other image buttons
def load_init(dir):
    global init_imageobj
    ### appending the path to the image name
    for image_name in os.listdir(dir):
        myfile = os.path.join(dir, image_name)
        if os.path.isfile(myfile):
            init_imageobj.append(ImageOBJ(myfile))



### opening the IR/MS layout
def IR_MS_open():
    ### ALL FUNCTIONS
    ### opening a file on the top canvas
    def open_topimage():
        global curr_width, curr_height, image1, topimage
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.jpg')
        ### opens the image
        topimage = ImageOBJ(root.filename)
        resize_ratio = 1

        ### image dimenisions check for scaling
        if topimage.orignal.height > (root.winfo_screenheight()*.46):
            resize_ratio = (topimage.orignal.height/((root.winfo_screenheight()*.46)))
        else:
            if topimage.orignal.width > (root.winfo_screenwidth() - 200):
                resize_ratio = (topimage.orignal.width/(root.winfo_screenwidth() - 200))

        ### resizing the image
        curr_width = int(topimage.orignal.width/resize_ratio)
        curr_height = int(topimage.orignal.height/resize_ratio)
        topimage.currVersion = topimage.currVersion.resize((curr_width, curr_height), Image.ANTIALIAS)
        topimage.update()
        ### create image at center of canvas
        image1 = my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int((root.winfo_screenheight()*.46)/2), image=topimage.pilcurrVersion)
    
    
    
    
     ### adds image to the bottom canvas
    def open_bottomimage():
        global curr_width, curr_height, bottomimage, image2
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.jpg')
        ### opens the image
        bottomimage = ImageOBJ(root.filename)
        resize_ratio = 1

        ### image dimenisions check for scaling
        if bottomimage.orignal.height > (root.winfo_screenheight()*.46):
            resize_ratio = (bottomimage.orignal.height/(root.winfo_screenheight()*.46))
        else:
            if bottomimage.orignal.width > (root.winfo_screenwidth() - 200):
                resize_ratio = (bottomimage.orignal.width/(root.winfo_screenwidth() - 200))

        ### resize image
        curr_width = int(bottomimage.orignal.width/resize_ratio)
        curr_height = int(bottomimage.orignal.height/resize_ratio)
        bottomimage.currVersion = bottomimage.currVersion.resize((curr_width,curr_height), Image.ANTIALIAS)
        bottomimage.update()
        ### create image at center of canvas
        image2 = sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(((root.winfo_screenheight()*.46))/2), image=bottomimage.pilcurrVersion)

    ### used to swap other image buttons for the image on canvas
    def swap(i):
        global bottomimage, image2, btns, init_imageobj
        temp = bottomimage
        bottomimage = init_imageobj[i]
        init_imageobj[i] = temp

        ### resize image
        resize_ratio = 1
        curr_width = int(bottomimage.orignal.width/resize_ratio)
        curr_height = int(bottomimage.orignal.height/resize_ratio)
        bottomimage.currVersion = bottomimage.currVersion.resize((curr_width, curr_height), Image.ANTIALIAS)
        bottomimage.update()
        
        sec_canvas.itemconfig(image2, image=bottomimage.pilcurrVersion)
        btns[i].config(image=init_imageobj[i].pilThumbnail)

    ### zoom in func
    def zoom():
        topimage.ImageScale(2)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=topimage.pilcurrVersion)

    # bottom canvas
    def zoom2():
        bottomimage.ImageScale(2)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=bottomimage.pilcurrVersion)

    ### zoom out
    def zoom_out():
        topimage.ImageScale(0.5)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=topimage.pilcurrVersion)

    def zoom_out2():
        bottomimage.ImageScale(0.5)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)),int(330/2), image=bottomimage.pilcurrVersion)

    ### used to get the coordinates for the draw func
    def get_x_and_y(event):
        global lasx, lasy
        lasx = event.x
        lasy = event.y

    ### drawing function
    def paint(event):
        global drawing, image1, topimage, lasx, lasy
        if is_draw_enable == TRUE:
            realdrawing = ImageDraw.Draw(topimage.drawingCanvas)
            realdrawing.line((lasx, lasy, event.x, event.y), fill="Red")
            topimage.update()
            my_canvas.itemconfig(image1, image=topimage.pilcurrVersion)
            lasx, lasy = event.x, event.y

    ### for bottom canvas too
    def paint2(event):
        global drawing, image2, bottomimage
        if is_draw_enable == TRUE:
            realdrawing = ImageDraw.Draw(bottomimage.drawingCanvas)
            realdrawing.line((lasx, lasy, event.x, event.y), fill="Red")
            bottomimage.update()
            sec_canvas.itemconfig(image2, image=bottomimage.pilcurrVersion)
            lasx, lasy = event.x, event.y
    
    ### turns the drawing feature on and off
    def toggle_draw():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            ### binds the mouse button movement to getting the coordinates
            my_canvas.bind('<Button-1>', get_x_and_y)
            ### binds the mouse movement to the line drawing
            my_canvas.bind('<B1-Motion>', paint)
        else:
            is_draw_enable = FALSE

    ### for bottom canvas too
    def toggle_draw2():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            ### binds the mouse button movement to getting the coordinates
            sec_canvas.bind('<Button-1>', get_x_and_y)
            ### binds the mouse movement to the line drawing
            sec_canvas.bind('<B1-Motion>', paint2)
        else:
            is_draw_enable = FALSE

    ### consider an erase feature???????

    ### IR table
    def open_IR():
        IR_root = Toplevel()  ### naming the variable and creates a Tk class
        IR_root.title('IR Table')
        IR_canvas = Canvas(IR_root, height = 400, width = 600, background='White')
        IR_canvas.pack()
        IR_img = tkinter.PhotoImage(file="IRtable.png")
        IR_label = Label(image=IR_img)
        IR_canvas.create_image(300, 200, image=IR_img)
        IR_root.mainloop()
    
    ### MS table with losses
    def open_MS():
        MS_root = Toplevel()  ### naming the variable and creates a Tk class
        MS_root.title('Logical MS Losses')
        MS_canvas = Canvas(MS_root, height = 400, width = 600, background='White')
        MS_canvas.pack()
        MS_img = tkinter.PhotoImage(file="MSloses.png")
        MS_label = Label(image=MS_img)
        MS_canvas.create_image(300, 200, image=MS_img)
        MS_root.mainloop()







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

    MS_button = ttk.Button(content, text = 'MS Losses', command=open_MS)
    MS_button.grid(row=17, column=0)

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

    ### to add an image into the top canvas :)
    add_image = ttk.Button(content, text='Add Image', command=open_topimage)
    add_image.grid(column=0, row=0)

    ### adds image to the bottom canvas
    add_image = ttk.Button(content, text='Add Image', command=open_bottomimage)
    add_image.grid(column=0, row=11)





    ### buttons for other images in directory
    load_init('IRMS')
    global btns
    btns = []
    for i in range(len(init_imageobj)):
        print(init_imageobj[i])
        btn = ttk.Button(content, text="ree", image=(init_imageobj[i].pilThumbnail),command=partial(swap, i))
        btn.grid(column=6, row=1+i)
        btns.append(btn)

    ### CANVASES
    ### for unknown spectra!
    my_canvas = tkinter.Canvas(content, height=((root.winfo_screenheight()*.46)), width=(root.winfo_screenwidth() - 200), background = 'White')
    my_canvas.grid(column=2, row=0, columnspan=3, rowspan=10)

    ### for known spectra!
    sec_canvas = tkinter.Canvas(content, height=((root.winfo_screenheight()*.46)), width=(root.winfo_screenwidth() - 200), background = 'White')
    sec_canvas.grid(column=2, row=11, columnspan=3, rowspan=10)







### opening fingerprint layout
def fingerprint_open():



### CANVASES
    ### for unknown spectra!
    my_canvas = tkinter.Canvas(content, background='white', height=int((root.winfo_screenheight()*.85)), width=int(((root.winfo_screenwidth() - 200)/2)))
    my_canvas.grid(column=1, row=0, columnspan=4, rowspan=10)
    x = (root.winfo_screenwidth() - 200)/2
    y = root.winfo_screenheight()*.85

    ### for known spectra!
    sec_canvas = tkinter.Canvas(content, background='white',height=int((root.winfo_screenheight()*.85)), width=int(((root.winfo_screenwidth() - 200)/2)))
    sec_canvas.grid(column=6, row=0, columnspan=4, rowspan=10)





    ### ALL FUNCTIONS
    ### opening a file on the top canvas
    def open_leftimage():
        global curr_width, curr_height, image1, leftimage
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        leftimage = ImageOBJ(root.filename)
        resize_ratio = 1

     
        ### image dimenisions check for scaling...
        if leftimage.orignal.height > ((root.winfo_screenheight()*.85)):
            resize_ratio = (leftimage.orignal.height/(root.winfo_screenheight()*.85))
        else:
            if leftimage.orignal.width > ((root.winfo_screenwidth()-200)/2):
                resize_ratio = (leftimage.orignal.width/((root.winfo_screenwidth()-200)/2))

        ### resizing the image
        curr_width = int(leftimage.orignal.width/resize_ratio)
        curr_height = int(leftimage.orignal.height/resize_ratio)
        leftimage.currVersion = leftimage.currVersion.resize((curr_width, curr_height), Image.ANTIALIAS)
        leftimage.update()
        ### create image at center of canvas
        image1 = my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=leftimage.pilcurrVersion)

    ### adds image to the bottom canvas
    def open_rightimage():
        global curr_width, curr_height, rightimage, image2
        root.filename = fd.askopenfilename(initialdir='c:', title='Select a File', type='*.png')
        ### opens the image
        rightimage = ImageOBJ(root.filename)
        resize_ratio = 1

     
        ### image dimenisions check for scaling...
        if rightimage.orignal.height > ((root.winfo_screenheight()*.85)):
            resize_ratio = (rightimage.orignal.height/(root.winfo_screenheight()*.85))
        else:
            if rightimage.orignal.width > ((root.winfo_screenwidth()-200)/2):
                resize_ratio = (rightimage.orignal.width/((root.winfo_screenwidth()-200)/2))

        ### resizing the image
        curr_width = int(rightimage.orignal.width/resize_ratio)
        curr_height = int(rightimage.orignal.height/resize_ratio)
        rightimage.currVersion = rightimage.currVersion.resize((curr_width, curr_height), Image.ANTIALIAS)
        rightimage.update()
        ### create image at center of canvas
        image2 = sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=rightimage.pilcurrVersion)
    
    ### zoom in and out
    def zoom():
        leftimage.ImageScale(2)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=leftimage.pilcurrVersion)

    # bottom canvas
    def zoom2():
        rightimage.ImageScale(2)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=rightimage.pilcurrVersion)

    ### zoom out
    def zoom_out():
        leftimage.ImageScale(0.5)
        my_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=leftimage.pilcurrVersion)

    def zoom_out2():
        rightimage.ImageScale(0.5)
        sec_canvas.create_image(int(((root.winfo_screenwidth() - 200)/2)/2),int((root.winfo_screenheight()*.85)/2), image=rightimage.pilcurrVersion)

    ### used to swap other image buttons for the image on canvas
    def swap(i):
        global rightimage, image2, btns, init_imageobj
        temp = rightimage
        rightimage = init_imageobj[i]
        init_imageobj[i] = temp

        ### resize image
        resize_ratio = 1
        curr_width = int(rightimage.orignal.width/resize_ratio)
        curr_height = int(rightimage.orignal.height/resize_ratio)
        rightimage.currVersion = rightimage.currVersion.resize((curr_width, curr_height), Image.ANTIALIAS)
        rightimage.update()
        
        sec_canvas.itemconfig(image2, image=rightimage.pilcurrVersion)
        btns[i].config(image=init_imageobj[i].pilThumbnail)

    ### used to get the coordinates for the draw func
    def get_x_and_y(event):
        global lasx, lasy
        lasx = event.x
        lasy = event.y

    ### drawing function
    def paint(event):
        global image1, leftimage, lasx, lasy
        if is_draw_enable == TRUE:
            realdrawing = ImageDraw.Draw(leftimage.drawingCanvas)
            realdrawing.line((lasx, lasy, event.x, event.y), fill="Red")
            leftimage.update()
            my_canvas.itemconfig(image1, image=leftimage.pilcurrVersion)
            lasx, lasy = event.x, event.y

    ### for bottom canvas too
    def paint2(event):
        global image2, rightimage, lasx, lasy
        if is_draw_enable == TRUE:
            realdrawing = ImageDraw.Draw(rightimage.drawingCanvas)
            realdrawing.line((lasx, lasy, event.x, event.y), fill="Red")
            rightimage.update()
            sec_canvas.itemconfig(image2, image=rightimage.pilcurrVersion)
            lasx, lasy = event.x, event.y


    ### turns the drawing feature on and off
    def toggle_draw():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            ### binds the mouse button movement to getting the coordinates
            my_canvas.bind('<Button-1>', get_x_and_y)
            ### binds the mouse movement to the line drawing
            my_canvas.bind('<B1-Motion>', paint)
        else:
            is_draw_enable = FALSE
            ### gives the mouse back to the move func
            my_canvas.bind('<B1-Motion>', move)

    ### for bottom canvas too
    def toggle_draw2():
        global is_draw_enable
        if is_draw_enable == FALSE:
            is_draw_enable = TRUE
            ### binds the mouse button movement to getting the coordinates
            sec_canvas.bind('<Button-1>', get_x_and_y)
            ### binds the mouse movement to the line drawing
            sec_canvas.bind('<B1-Motion>', paint2)
        else:
            is_draw_enable = FALSE
            ### gives the mouse back to the move func
            sec_canvas.bind('<B1-Motion>', move2)

    ### erase feature in future????

    ### allows the image to move within the canvas
    def move(event):
        global leftimage
        ### deletes the current image
        my_canvas.delete('all')
        ### creates a new image
        my_canvas.create_image(event.x, event.y, image=leftimage.pilcurrVersion)
        
    ### bind the move function to mouse movement
    my_canvas.bind('<B1-Motion>', move)

    ### for the second canvas :)
    def move2(event):
        global rightimage
        ### deletes the current image on canvas
        sec_canvas.delete('all')
        ### creates a new image where you moved
        sec_canvas.create_image(event.x, event.y, image=rightimage.pilcurrVersion)

    ### bind the move function to the mouse movement
    sec_canvas.bind('<B1-Motion>', move2)




        ### editing options buttons and their positions
    ### figure out how to turn it back on
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw)
    draw_button.grid(row=10, column=4)

    # for bottom canvas
    draw_button = ttk.Button(content, text = "Draw", command=toggle_draw2)
    draw_button.grid(row=10, column=9)

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

    ### to add an image into the top canvas :)
    add_image = ttk.Button(content, text='Add Image', command=open_leftimage)
    add_image.grid(column=1, row=10)

    ### adds image to the bottom canvas
    add_image = ttk.Button(content, text='Add Image', command=open_rightimage)
    add_image.grid(column=6, row=10)


    ### buttons for other images in directory
    load_init('fps')
    global btns
    btns = []
    for i in range(len(init_imageobj)):
        btn = ttk.Button(content, image=(init_imageobj[i].pilThumbnail), command=partial(swap, i))
        btn.grid(column=11, row=1+i)
        btns.append(btn)



### creating a menu
menubar = Menu(root, background='dark grey', foreground='black', activebackground='dark grey', activeforeground='black')
### file menu option
file = Menu(menubar, tearoff=0)

sub_menu = Menu(file, tearoff=0)
sub_menu.add_command(label='IR/MS', command=IR_MS_open)
sub_menu.add_command(label='Fingerprints', command=fingerprint_open)

file.add_cascade(label='New', menu=sub_menu)

file.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='File', menu=file)


root.config(menu=menubar)



root.mainloop()  ### displays everything until the program is closed!