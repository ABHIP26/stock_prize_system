from Tkinter import *
from PIL import ImageTk, Image



class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.grid()
        self.FirstFrame()

    def FirstFrame(self):
        Frame.__init__(self)

        self.img = ImageTk.PhotoImage(Image.open('stok.jpg'))
        self.panel = Label(self, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")

        self.button = Button(self, text="Let's Get in",bg="Red", command=self.Login)
        self.button.pack(side=RIGHT)

        self.pack()

    def Login(self):
        Frame.__init__(self)

        self.pack()


root = Tk()
ap = Application(root)
root.title("Stock Prize Predictor System")
root.geometry("270x210")
root.mainloop()

