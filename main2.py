#Importing library
import tkinter as tk
#from PIL import ImageTk,Image

#define functions
FunctionList = [
    "Create User",
    "Create Users"
]
app = tk.Tk()

app.geometry('600x100')

variable = tk.StringVar(app)
variable.set(FunctionList[0])

opt = tk.OptionMenu(app, variable, *FunctionList)
opt.config(width=90, font=('terminal', 12))
opt.pack(side="top")

#Label
labelTest = tk.Label(text="",font=('terminal', 12), fg='red')
labelTest.pack(side="top")

#function
def callback(*args):
    labelTest.configure(text="The Function You Have Selected {}".format(variable.get()))

variable.trace("w",callback)

app.mainloop()