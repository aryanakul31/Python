import tkinter
from tkinter import *

win=Tk()
cb1=IntVar()
cb=Checkbutton(win,text='Music',offvalue=0,onvalue=1,height=5,width=10,variable=cb1)
cb.pack()

var=IntVar()
rb=Radiobutton(win,text='Option1',variable=var,value=1)
rb.pack()
rb2=Radiobutton(win,text='Option2',variable=var,value=2)
rb2.pack()
rb3=Radiobutton(win,text='Option3',variable=var,value=3)
rb3.pack()
win.mainloop()