import tkinter
from tkinter import *
from tkinter import messagebox

win=Tk()

def hello():
    messagebox.showinfo(title='from computer',message='hello')

b=Button(win, text="PopUp",command=hello)
b.pack()

win.mainloop()