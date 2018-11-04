#used to generate gui, able to resize, close windows created, not very popular to use
#also able to create buttons, menus, ...

from tkinter import *
from PIL import Image, ImageTk

#creating a windows class
class Window(Frame):   #class frame exists in __init__
    def __init__(self, master = None):
        Frame.__init__(self, master) #creating a default 
        self.master = master
        self.init_window()

##adding buttons, titles to created window, initializing them
    def init_window(self):
        self.master.title("GUI") #Initial title for the window
        self.pack(fill=BOTH, expand=1)#fill up the window and adjust
        #quitButton = Button(self, text="quit" ,command=self.client_exit) #part of Tkinter, search in module
        #quitButton.place(x=0, y=0)
        #creating a menu bar instead of just a quit button
        menubar = Menu(self.master) #Menu is part of the module tkinter
        self.master.config(menu=menubar) #defining the instance of the menu

        file = Menu(menubar)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menubar.add_cascade(label='File', menu=file) #creates a cascading menu with the option of exit

        edit = Menu(menubar)
        edit.add_command(label='Show Image', command=self.showImg) #just to add otions to menus
        edit.add_command(label='Show Text', command=self.showTxt)
        menubar.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        root.destroy()

    def showImg(self):
        load = Image.open("TKinter\Python.jpg")
        render = ImageTk.PhotoImage(load) #renders the image to be loaded
        img = Label(self, image=render)
        img.image = render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self, text='Hello there')
        text.pack()

root = Tk()
root.geometry("400x300") #specifies the default window size

app = Window(root)

root.mainloop() #initializes and frames the window, this window can resize , move and closes
