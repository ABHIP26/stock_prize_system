import Tkinter
class Cookbook(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title("Cookbook")
        self.geometry("500x500+0+0")

        self.button = []
        for r in range(1):
            for c in range(1):
                b = Button(self).grid(row=r,column=c)
                self.button.append(b)

class Button(Tkinter.Button):
    def __init__(self,parent):
            b = Tkinter.Button.__init__(self, parent, text="Add A New Recipie", height=8, width=15, command=self.make_window)

    def make_window(self):
        popwindow = Recipie()
        popwindow.name()
        popwindow.ingredients()
        popwindow.addingredient()
        popwindow.savebutton()
        popwindow.save()

class Recipie(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title("New Recipie")
        self.geometry("500x500")

    def name(self):
        name = Tkinter.Label(self, text="Title:")
        name.pack() #used to be name.place(anchor="nw")

        self.insert_name = Tkinter.Entry(self) #edited with the answer below, used to be insert_name = Tkinter.Entry(self)
        self.insert_name.pack() #edited with the answer from below, used to be insert_name.pack()
        self.insert_name.focus_set() #edited with the answer from below, used to be insert_name.focus_set()

    def ingredients(self):
        self.e = Tkinter.Entry(self) #edited with the answer from below, used to be e.get()
        self.e.pack() #edited with the answer from below, used to be e.pack()
        self.e.focus_set() #edited with the answer from below, used to be e.focus_set()

    def addingredient(self):
        but = Tkinter.Button(self, text="Add Ingredients", width=15, command=self.ingredients)
        but.pack(side="bottom")

    def procedure(self):
        txt = Tkinter.Label(self, text="List the Steps:")
        txt.place(anchor="n")

        self.p = Tkinter.Entry(self) #edited with the answer from below, used to be p = Tkinter.Entry(self)
        self.p.place(anchor="nw") #edited with the answer from below, used to be p.place(anchor="nw")
        self.p.focus_set() #edited with the answer from below, used to be p.focus_set

    def savebutton(self):
        print self.insert_name.get() #edited with the answer from below
        print self.e.get() #edited with the answer from below
        print self.p.get() #edited with the answer from below

    def save(self):
         b = Tkinter.Button(self, text="Save Recipie", width=15,command=self.savebutton)
         b.pack()

top = Cookbook()
top.mainloop()