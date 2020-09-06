import tkinter
from tkinter import *

win=Tk()

def nothing():
    file=Toplevel(win)
    btn=Button(file,text="Do Nothing")
    btn.pack()

menuBar=Menu(win)

fileMenu=Menu(menuBar)
fileMenu.add_command(label='New File',command=nothing)
fileMenu.add_command(label='Open File',command=nothing)
fileMenu.add_separator()
fileMenu.add_command(label='Close File',command=nothing)
fileMenu.add_command(label='Save File',command=nothing)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=win.quit)

menuBar.add_cascade(label='File',menu=fileMenu)

editMenu=Menu(menuBar)
editMenu.add_command(label='Undo',command=nothing)
editMenu.add_command(label='Copy',command=nothing)
editMenu.add_separator()
editMenu.add_command(label='Paste',command=nothing)
editMenu.add_command(label='Cut',command=nothing)
editMenu.add_separator()
editMenu.add_command(label='Exit',command=win.quit)

menuBar.add_cascade(label='Edit',menu=editMenu)

win.config(menu=menuBar)


# mb=Menubutton(win,text='File')
# mb.grid()
# mb.menu=Menu(mb)
# mb['menu']=mb.menu

# x1=IntVar()
# x2=IntVar()

# mb.menu.add_checkbutton(label='Open',variable=x1)
# mb.menu.add_checkbutton(label='Close',variable=x2)
# mb.pack()
win.mainloop()