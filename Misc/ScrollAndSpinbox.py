import tkinter
from tkinter import *

win=Tk()

scroll=Scale(win)
scroll.pack()

sb=Spinbox(win,from_=0,to_=10)
sb.pack(side=RIGHT,fill=Y)

scrollbar=Scrollbar(win)
list=Listbox(win,yscrollcommand=scrollbar.set)
for line in range(100):
    list.insert(END,'This is line no '+str(line))

list.pack()
win.mainloop()