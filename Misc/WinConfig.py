import tkinter
from tkinter import *

win=Tk()
frame=Frame(win)
frame.pack()

frame2=Frame(win)
frame2.pack(side=BOTTOM)

rb=Button(frame,text="Red",fg="Red")
rb.pack(side=LEFT)
bb=Button(frame,text="Black",fg="black")
bb.pack(side=RIGHT)

gb=Button(frame2,text="Green",fg='green')
gb.pack(side=LEFT)

win.mainloop()