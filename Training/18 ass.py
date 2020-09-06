import tkinter as tk

class MyWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.master.title("Login")
        self.master.geometry("300x250")
        self.create_login()

    def create_login(self):
        self.l1=tk.Label(self.master,text="LOGIN PAGE",fg="black")
        self.l1.pack()

        self.userValue= tk.StringVar()
        self.l2=tk.Label(self.master,text="Username",fg="black")
        self.l2.pack(pady=15) #external padding, vertically
        self.e2=tk.Entry(self.master,width=20, textvariable= self.userValue)
        self.e2.pack()

        self.passwordValue= tk.StringVar()
        self.l3=tk.Label(self.master,text="Password",fg="black")
        self.l3.pack(pady=15) #external padding, vertically
        self.e3=tk.Entry(self.master,width=20,  show='*', textvariable= self.passwordValue)
        self.e3.pack()

        self.b1=tk.Button(self.master,text="LOGIN",width=10, command=self.show)
        self.b1.pack(pady=15)

    def show(self):
        username= self.userValue.get()
        password= self.passwordValue.get()
        print("Username:",username)
        print("Password:",password)

def main():
    root = tk.Tk()
    app = MyWindow(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
