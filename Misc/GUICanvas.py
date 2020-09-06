import tkinter
from tkinter import *

win=Tk()

c=Canvas(win,height=250,width=300,bg='blue')
coor=10,50,240,240
arc=c.create_arc(coor,start=0,extent=150,fill='red')
line=c.create_line(10,10,200,200,fill='white')

c.pack()
win.mainloop()