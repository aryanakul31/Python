import tkinter
from tkinter import *

win=Tk()
lb=Listbox(win)
lb.insert(1,'python')
lb.insert(2,'java')
lb.insert(3,'Ruby')
lb.pack()
win.mainloop()