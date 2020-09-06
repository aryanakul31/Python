import tkinter
from tkinter import *

win=Tk()

# First Part
b=0
for i in range(6):
    for j in range(6):
        b=b+1
        Button(win,text=str(b),borderwidth=1).grid(row=i,column=j)

# Second Part
l1=Label(win,text='Maths')
l1.place(x=10,y=10)
e1=Entry(win,border=5)
e1.place(x=60,y=10)

win.mainloop()