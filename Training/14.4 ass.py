f=open("a.txt","r")
x=f.read(6)
print(x)

y=f.readline()
print(y)

z=f.readlines()
print(z)

f.close()
