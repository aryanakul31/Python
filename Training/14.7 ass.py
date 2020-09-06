f=open("a.txt","w")

l=[]
for i in range(10):
    a=input("enter a number:")
    b=str(a)
    l.append(b+"\n")

f.writelines(l)

f.close()
print(f.closed)
