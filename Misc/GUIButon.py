import tkinter 
from tkinter import *


def pr():
    print("Hi")

win=Tk()
win.geometry("400x400")
b=Button(win,text='Button',command=pr,padx=2,pady=2, activeforeground='red')
# b.pack()
# b.grid(row=1,column=1)
b.place(x=100,y=200)

b2=Button(win,text='Button 2')
# b2.pack()
# b2.grid(row=2,column=2)
b2.place(x=200,y=200)
win.mainloop()