import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser
import random
def run():
    while True:
        suff = "http://{}".format(link)
        webbrowser.open(suff)

def frezz():
    global link
    if CheckVar1.get()==1:
        link = random.choice(['google.com', 'utu.ac.in', 'app.utu.ac.in/EngineeringSIS/Login.aspx', 'app.utu.ac.in/stud/Login.aspx','cgpit-bardoli.edu.in'])
        run()
    else:
        link = random.choice(['google.com', 'google.com', 'google.com', 'google.com'])
        run()
def checkvalue():
    if CheckVar1.get() == 1:
        if (CheckVar2.get()) == 1:
            messagebox.showinfo("Warnning", "Plese select any one option")
            start.destroy()
            st()
    else:
        if CheckVar1.get() == 1:
            messagebox.showinfo("Warnning", "Plese select any one option")
            start.destroy()
            st()
def st():
    def spacing():
        Label(text=" ",bg="#E29484").pack()
        Label(text=" ",bg="#E29484").pack()
    global start
    start = tkinter.Tk()
    start.geometry('700x500')
    start.configure(bg="#E29484")
    start.title("frezz the system")
    Label(text=" Having just fun with the computer !!!", bg="black", fg="white", width="700", height="2", font=("Calibri", 18)).pack()
    spacing()
    global CheckVar1
    global CheckVar2
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    Checkbutton(start, text = "18 +", variable = CheckVar1, onvalue = 1, offvalue = 0, height=3,width = 20,command=checkvalue ).pack()
    Label(text=" or ", width="100", height="2", font=("Calibri", 25),bg="#E29484").pack()
    Checkbutton(start, text = "18 below", variable = CheckVar2,onvalue = 1, offvalue = 0, height=3,width = 20,command=checkvalue).pack()
    def check():
        if CheckVar1.get()==1 or CheckVar2.get()==1:
            frezz()
            start.destroy()
        else:
            messagebox.showinfo("Warnning", "Plese select option")
    spacing()
    spacing()
    Button(text="Process for frezz", width="50", height="2",command=check).pack()
    spacing()
    a=Label(start,text="if you are 18+ make sure run program in private space!!!", bg="white", fg="red", width="700",height="1", font=("Calibri", 10)).pack()
    start.mainloop()
st()