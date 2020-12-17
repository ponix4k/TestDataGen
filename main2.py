#Importing library
from tkinter import *
from tkinter import messagebox
import tkinter 
#from PIL import ImageTk,Image

class Example(Frame):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Test Data Generator")
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="New Database")
        submenu.add_command(label="Open Database")
        fileMenu.add_cascade(label='Import',menu=submenu, underline=0)
        helpMenu = Menu(menubar)
        submenu = Menu(helpMenu)
        
        #fileMenu.add_seperator()
        
        fileMenu.add_command(label="Exit",underline = 0,command=self.onExit)
        menubar.add_cascade(label="File",underline = 0, menu=fileMenu)
        
        helpMenu.add_command(label="About",underline = 0, menu = helpMenu)
        menubar.add_cascade(label="Help",underline = 0, menu = helpMenu)
    def onExit(self):
        self.quit()
    
    def openAbout():
        newWindow = Toplevel(app)
        newWindow.geometry("250x250")
        newWindow.title("About")
        newWindow.resizable = (False,False)
        lblAuth = Label(newWindow, text="John Williams")
        lblSite = Label(newWindow, text="https://projectmoonrope.co.uk")
        lblAuth.grid(row=1)
        lblSite.grid(row=4)
    
def main():
    root = Tk()
    root.title("Test Data Generator")
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()
    
if __name__ == '__main__':
    main()

#app.mainloop()