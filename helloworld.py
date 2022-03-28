from tkinter import *  ### Imports everything
from tkinter import ttk  ### imports the class tkinter.ttk so that I don't have to type that in everytime
root = Tk()  ### naming the variable and creates a Tk class
frm = ttk.Frame(root, padding=10)  ### window formation?
frm.grid()  ### used to format the widget window :)
ttk.Label(frm, text="Hello World!").grid(row=0, column=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=1, column=0)
root.mainloop()  ### displays everything until the program is closed!