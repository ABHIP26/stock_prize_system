from Tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("stocks.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
button = Button(root, text="Home", bg="red")
button.pack(side=RIGHT)
button2 = Button(root, text="About Us",bg="red")
button2.pack(side=RIGHT)
root.mainloop()