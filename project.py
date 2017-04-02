from Tkinter import *
from PIL import ImageTk, Image


class Project(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.img = ImageTk.PhotoImage(Image.open('stok.jpg'))
        self.panel = Label(self, image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")

        self.button = Button(self, text="Home", fg="red", bg="blue")
        self.button.grid(columnspan=2)
        self.button2 = Button(self, text="About Us", fg="red", bg="blue", command=self.AboutUs)
        self.button2.grid(columnspan=2)
        self.button3 = Button(self, text="LogIn", fg="red", bg="blue", command=self.LogIn)
        self.button3.grid(columnspan=5)

        self.pack(side=RIGHT)

    def AboutUs(self):
        Frame.__init__(self)
        self.button4 = Button(self, text="About Us", fg="red", bg="blue")
        self.button4.grid(columnspan=2, row=3)
        self.button5 = Button(self, text="LogIn", fg="red", bg="blue", command=self.LogIn)
        self.button5.grid(columnspan=2, row=4)

        self.label = Label(self,
                           text="This is a simple stock prizes predictor system\n based Linear Regression analysis method \n and it uses the technologies like python and mysql database")
        self.label.grid(row=1, sticky=E)

        self.pack(side=RIGHT)

    def LogIn(self):
        Frame.__init__(self)

        self.label2 = Label(self, text="Please Login In to The system")
        self.label3 = Label(self, text="Username")
        self.label3.grid(row=0, sticky=E)
        self.label4 = Label(self, text="Password")
        self.label4.grid(row=1, sticky=E)
        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)
        self.entry2 = Entry(self)
        self.entry2.grid(row=1, column=1)
        self.checkbutton = Checkbutton(self, text="Keep me logged in")
        self.checkbutton.grid(columnspan=2)
        self.button6 = Button(self, text="Login", command=self.Login_btn_clicked)
        self.button6.grid(columnspan=2)
        self.button7 = Button(self, text="Create an Account", fg="red", bg="blue", command=self.SignUp)
        self.button7.grid(columnspan=4)

        self.button8 = Button(self, text="Home", fg="red", bg="blue")
        self.button8.grid(columnspan=2)
        self.button9 = Button(self, text="About Us", fg="red", bg="blue", command=self.AboutUs)
        self.button9.grid(columnspan=2)

        self.pack(side=RIGHT)

    def SignUp(self):
        Frame.__init__(self)

        self.label5 = Label(self, text="Enter the credentials")
        self.label6 = Label(self, text="Username")
        self.label7 = Label(self, text="Name")
        self.label8 = Label(self, text="UIDAI No.")
        self.label9 = Label(self, text="Email Id")
        self.label10 = Label(self, text="Residential Address")
        self.label11 = Label(self, text="Permanant Address")
        self.label12 = Label(self, text="Mobile No.")
        self.label13 = Label(self, text="Company Name")
        self.label14 = Label(self, text="Password")
        self.label15 = Label(self, text="Confirm Password")
        self.entry3 = Entry(self)
        self.entry4 = Entry(self)
        self.entry5 = Entry(self)
        self.entry6 = Entry(self)
        self.entry7 = Entry(self)
        self.entry8 = Entry(self)
        self.entry9 = Entry(self)
        self.entry10 = Entry(self)
        self.entry11 = Entry(self, show="*")
        self.entry12 = Entry(self, show="*")
        self.label5.grid(row=1, sticky=E)
        self.label6.grid(row=2, sticky=E)
        self.label7.grid(row=3, sticky=E)
        self.label8.grid(row=4, sticky=E)
        self.label9.grid(row=5, sticky=E)
        self.label10.grid(row=6, sticky=E)
        self.label11.grid(row=7, sticky=E)
        self.label12.grid(row=8, sticky=E)
        self.label13.grid(row=9, sticky=E)
        self.label14.grid(row=10, sticky=E)
        self.label15.grid(row=11, sticky=E)
        self.entry3.grid(row=2, column=2)
        self.entry4.grid(row=3, column=2)
        self.entry5.grid(row=4, column=2)
        self.entry6.grid(row=5, column=2)
        self.entry7.grid(row=6, column=2)
        self.entry8.grid(row=7, column=2)
        self.entry9.grid(row=8, column=2)
        self.entry10.grid(row=9, column=2)
        self.entry11.grid(row=10, column=2)
        self.entry12.grid(row=11, column=2)
        self.checkbox2 = Checkbutton(self, text="I Agree Terms and Conditions ")
        self.checkbox2.grid(columnspan=2)

        self.button10 = Button(self, text="Create an Account", bg="blue", fg="red", command=self.signup_btn_clicked)
        self.button10.grid(columnspan=3)

        self.button11 = Button(self, text="Home", fg="red", bg="blue")
        self.button11.grid(columnspan=2)
        self.button12 = Button(self, text="About Us", fg="red", bg="blue", command=self.AboutUs)
        self.button12.grid(columnspan=2)

        self.pack(side=RIGHT)

    def signup_btn_clicked(self):
        Frame.__init__(self)

        addhim = open("User-Signup.txt", "w")
        addhim.write("\nUsername:" + self.entry3.get())
        addhim.write("\nname :" + self.entry4.get())
        addhim.write("\nUIDAI No" + self.entry5.get())
        addhim.write("\nEmail Id" + self.entry6.get())
        addhim.write("\nResidential Address :" + self.entry7.get())
        addhim.write("\nPermanant Address :" + self.entry8.get())
        addhim.write("\nMobile No. :" + self.entry9.get())
        addhim.write("\nCompany Name :" + self.entry10.get())
        addhim.write("\nPassword :" + self.entry11.get())
        addhim.write("\nRetype Passsword :" + self.entry12.get())
        addhim.close()

        self.button13 = Button(self, text="About Us", fg="red", bg="blue", command=self.AboutUs)
        self.button13.grid(columnspan=2)
        self.button14 = Button(self, text="Login", fg="red", bg="blue", command=self.LogIn)
        self.button14.grid(columnspan=2)

        self.pack()

    def Login_btn_clicked(self):
        Frame.__init__(self)

        adduser = open("User.txt", "w")
        adduser.write("User ID: " + self.entry.get())
        adduser.write("\nUser Password: " + self.entry2.get())
        adduser.close()

        self.button13 = Button(self, text="Dashboard", command=self.Dashboard())
        self.button13.grid(comunspan=2)
        self.pack()

    def Dashboard(self):
        Frame.__init__(self)
        self.pack()


root = Tk()
pr = Project(root)
root.mainloop()
