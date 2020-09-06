import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle


class MyWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.master.title("Pizza Frame")
        self.master.geometry("800x700")
        self.master.configure(bg='black')
        style=ThemedStyle(self.master)
        style.set_theme("black")
        self.create_widgets()

    def create_widgets(self):
        self.l=ttk.Label(self.master,text="WELCOME TO PIZZA MANIA",background='black',foreground="white",font="Bahnschrift 28")
        self.l.pack()
        self.l1=ttk.Label(self.master,text="TOPPINGS @55 each",background='black',foreground="white",font="Caladea 18")
        self.l1.place(x=25,y=65)
        self.l2=ttk.Label(self.master,text="PIZZA SIZE",background='black',foreground="white",font="Caladea 18")
        self.l2.place(x=375,y=65)
        self.l3=ttk.Label(self.master,text="PIZZA TYPE",background='black',foreground="white",font="Caladea 18")
        self.l3.place(x=600,y=65)
                
        self.Var1=tk.StringVar()
        self.Var2=tk.StringVar()
        self.Var3=tk.StringVar()
        self.Var4=tk.StringVar()
        self.Var5=tk.StringVar()
        self.Var6=tk.StringVar()
        self.Var7=tk.StringVar()
        self.Var8=tk.StringVar()
        self.ch1=ttk.Checkbutton(self.master,onvalue='Mushrooms',variable=self.Var1,text='Mushrooms')
        self.ch1.place(x=25,y=115)
        self.ch2=ttk.Checkbutton(self.master,onvalue='Onions',variable=self.Var2,text='Onions')
        self.ch2.place(x=25,y=155)
        self.ch3=ttk.Checkbutton(self.master,onvalue='Capsicums',variable=self.Var3,text='Capsicums')
        self.ch3.place(x=25,y=195)
        self.ch4=ttk.Checkbutton(self.master,onvalue='Tomatos',variable=self.Var4,text='Tomatos')
        self.ch4.place(x=25,y=235)
        self.ch5=ttk.Checkbutton(self.master,onvalue='Olives',variable=self.Var5,text='Olives')
        self.ch5.place(x=25,y=275)
        self.ch6=ttk.Checkbutton(self.master,onvalue='Jalapenos',variable=self.Var6,text='Jalapenos')
        self.ch6.place(x=25,y=315)
        self.ch7=ttk.Checkbutton(self.master,onvalue='Paneer',variable=self.Var7,text='Paneer')
        self.ch7.place(x=25,y=355)
        self.ch8=ttk.Checkbutton(self.master,onvalue='Sweet corn',variable=self.Var8,text='Sweet corn')
        self.ch8.place(x=25,y=395)
        
        self.x=tk.StringVar()
        self.a1=ttk.Radiobutton(self.master,value='250',variable=self.x,text='Small Rs.250')
        self.a1.place(x=375,y=115)
        self.a2=ttk.Radiobutton(self.master,value='375',variable=self.x,text='Medium Rs.375')
        self.a2.place(x=375,y=155)
        self.a3=ttk.Radiobutton(self.master,value='500',variable=self.x,text='Large Rs.500')
        self.a3.place(x=375,y=195)

        self.y=tk.StringVar()
        self.r1=ttk.Radiobutton(self.master,value='40',variable=self.y,text='Classic Hand Tossed Rs.40')
        self.r1.place(x=600,y=115)
        self.r2=ttk.Radiobutton(self.master,value='60',variable=self.y,text='Pan Pizza Rs.60')
        self.r2.place(x=600,y=155)
        self.r3=ttk.Radiobutton(self.master,value='65',variable=self.y,text='Thin Crust R.65')
        self.r3.place(x=600,y=195)
        self.r4=ttk.Radiobutton(self.master,value='80',variable=self.y,text='Cheese Burst Rs.80')
        self.r4.place(x=600,y=235)

        self.b=ttk.Button(self.master,text='PLACE ORDER', command=self.amount)
        self.b.place(x=350,y=425,width=110)

        self.outputText= tk.StringVar()
        self.output=ttk.Label(self.master,background='black',foreground="white",font="Caladea 15",textvariable=self.outputText)
        self.output.place(x=200,y=475)

    def amount(self):        
        toppings=list()
        if len(self.Var1.get())>1:
            toppings.append(self.Var1.get())
        if len(self.Var2.get())>1:
            toppings.append(self.Var2.get())
        if len(self.Var3.get())>1:
            toppings.append(self.Var3.get())
        if len(self.Var4.get())>1:
            toppings.append(self.Var4.get())
        if len(self.Var5.get())>1:
            toppings.append(self.Var5.get())
        if len(self.Var6.get())>1:
            toppings.append(self.Var6.get())
        if len(self.Var7.get())>1:
            toppings.append(self.Var7.get())
        if len(self.Var8.get())>1:
            toppings.append(self.Var8.get())

        toppingsAmount=len(toppings)*55
        pizzaSizeAmount= int(self.x.get())
        pizzaTypeAmount= int(self.y.get())
        totalAmount= toppingsAmount+pizzaSizeAmount+pizzaTypeAmount

        pizzaType=''
        if pizzaTypeAmount==40:
            pizzaType='Classic Hand Tossed'
        elif pizzaTypeAmount==60:
            pizzaType='Pan Pizza'
        elif pizzaTypeAmount==65:
            pizzaType='Thin Crust'
        elif pizzaTypeAmount==80:
            pizzaType='Cheese Burst'

        pizzaSize=''
        if pizzaSizeAmount==250:
            pizzaSize='Small'
        elif pizzaSizeAmount==375:
            pizzaSize='Medium'
        elif pizzaSizeAmount==500:
            pizzaSize='Large'
        
        text= 'Pizza Type: '+pizzaType+'\nPizza Size: '+pizzaSize+'\nToppings: '+str(toppings)+'\nTotal Amount: Rs'+str(totalAmount)
        self.outputText.set(text)


def main():
    root=tk.Tk()
    app=MyWindow(master=root)
    app.mainloop()

if __name__=="__main__":
    main()
