import tkinter
from tkinter import *

win=Tk()
l=Label(win,text='Username')
# l.pack()
l.grid(row=1,column=1)
e=Entry(win)
# e.pack()
e.grid(row=1,column=2)
t=Text(win)
t.insert(INSERT,'hello')
t.grid(row=2,column=1)
win.mainloop()