# -- imports --#

from Tkinter import *
from PIL import ImageTk, Image
import os

# -- windows title --#
window = Tk()
window.title("Stock Prize Predictor System")
# -- windows geometry --#
window.geometry("270x210")
# --windows background --#
window.configure(bg="gray")

# -- Main Frame --#

# -- The Image --#
img = ImageTk.PhotoImage(Image.open('login_background.jpeg'))
panel = Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")


def donothing():
    filewin = Toplevel(window)
    button = Button(filewin, text="Do nothing button")
    button.pack()


# -- The Menu Bar --#


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# -- edit menu --#
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

# -- PrePocessing Tab --#

preprocessing = Menu(menubar, tearoff=0)
preprocessing.add_command(label="Undo", command=donothing)

menubar.add_cascade(label="Preprocessing", menu=preprocessing)

# -- Login/SignUp -- #

login = Menu(menubar, tearoff=0)
login.add_command(label="Undo", command=donothing)

login.add_separator()
login.add_command(label="SignUp", command=donothing)

menubar.add_cascade(label="LogIn", menu=login)
# -- Help Menu --#
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

window.mainloop()
