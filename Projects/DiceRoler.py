import random

n=input("Roll the dice? Y | N\n")

while n.lower()=="y":
    number=random.randint(1,6)
    if number==1:
        print("_______")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("_______")
    
    if number==2:
        print("_______")
        print("|  0  |")
        print("|     |")
        print("|  0  |")
        print("_______")

    if number==3:
        print("_______")
        print("|0    |")
        print("|  0  |")
        print("|    0|")
        print("_______")

    if number==4:
        print("_______")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("_______")

    if number==5:
        print("_______")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("_______")

    if number==6:
        print("_______")
        print("|0   0|")
        print("|0   0|")
        print("|0   0|")
        print("_______")

    n=input("Roll the dice? Y | N\n")