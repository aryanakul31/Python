import tkinter as tk

class MyWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.master.title("Converter Frame")
        self.master.geometry("300x250")
        self.create_login()

    def create_login(self):
        self.l1=tk.Label(self.master,text="CONVERTER",fg="black")
        self.l1.pack()

        self.inchValue = tk.StringVar()
        self.l2=tk.Label(self.master,text="Lenth in inches",fg="black")
        self.l2.pack(pady=15) #external padding, vertically
        self.e2=tk.Entry(self.master,width=20, textvariable= self.inchValue)
        self.e2.pack()        

        self.b1=tk.Button(self.master,text="CONVERT",width=10, command=self.convert)
        self.b1.pack(pady=10)
    
        self.centimeterValue= tk.StringVar()
        self.l3=tk.Label(self.master,text="Lenth in centimeters",fg="black")
        self.l3.pack(pady=15) #external padding, vertically
        self.e3=tk.Entry(self.master,width=20, textvariable=self.centimeterValue)
        self.e3.pack()

    def convert(self):    
        value= float(self.inchValue.get())*2.54
        self.centimeterValue.set(value)


def main():
    root = tk.Tk()
    app = MyWindow(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()