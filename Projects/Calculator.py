from tkinter import *

expression = ""


def calc(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalPress():
    global expression

    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("Error")


def reset():
    equation.set("")
    global expression
    expression = ""


if __name__ == "__main__":
    master = Tk()
    master.configure(background="light green")
    master.title("Calculator")
    master.geometry("260x240")

    equation = StringVar()

    # Entry for results
    expression_field = Entry(master, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)
    equation.set("")

    # Numbers
    b0 = Button(master, text="0", command=lambda: calc("0"), height=3, width=5)
    b0.grid(row=1, column=0, sticky='nesw')
    b1 = Button(master, text="1", command=lambda: calc("1"), height=3, width=5)
    b1.grid(row=1, column=1, sticky='nesw')
    b2 = Button(master, text="2", command=lambda: calc("2"), height=3, width=5)
    b2.grid(row=1, column=2, sticky='nesw')
    b3 = Button(master, text="3", command=lambda: calc("3"), height=3, width=5)
    b3.grid(row=2, column=0, sticky='nesw')
    b4 = Button(master, text="4", command=lambda: calc("4"), height=3, width=5)
    b4.grid(row=2, column=1, sticky='nesw')
    b5 = Button(master, text="5", command=lambda: calc("5"), height=3, width=5)
    b5.grid(row=2, column=2, sticky='nesw')
    b6 = Button(master, text="6", command=lambda: calc("6"), height=3, width=5)
    b6.grid(row=3, column=0, sticky='nesw')
    b7 = Button(master, text="7", command=lambda: calc("7"), height=3, width=5)
    b7.grid(row=3, column=1, sticky='nesw')
    b8 = Button(master, text="8", command=lambda: calc("8"), height=3, width=5)
    b8.grid(row=3, column=2, sticky='nesw')
    b9 = Button(master, text="9", command=lambda: calc("9"), height=3, width=5)
    b9.grid(row=4, column=0, sticky='nesw')

    # Operator
    plus = Button(master, text="+", command=lambda: calc("+"), height=3, width=5)
    plus.grid(row=1, column=3, sticky='nesw')
    minus = Button(master, text="-", command=lambda: calc("-"), height=3, width=5)
    minus.grid(row=2, column=3, sticky='nesw')
    multiple = Button(master, text="*", command=lambda: calc("*"), height=3, width=5)
    multiple.grid(row=3, column=3, sticky='nesw')
    divide = Button(master, text="/", command=lambda: calc("/"), height=3, width=5)
    divide.grid(row=4, column=1, sticky='nesw')
    equal = Button(master, text="=", command=lambda: equalPress(), height=3, width=5)
    equal.grid(row=4, column=2, sticky='nesw')

    clear = Button(master, text="C", command=lambda: reset(), height=3, width=5)
    clear.grid(row=4, column=3, sticky='nesw')

    master.resizable(0, 0)
    master.mainloop()
