file=open("a.txt","r")
x=list()
for sentence in file:
    x.append(file.readlines())
print(x)
y=sorted(x)
print(y)
file.close()
print(file.closed)
