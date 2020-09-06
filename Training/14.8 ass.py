file=open("a.txt","r")
list=[]
total=0
for line in file:
    list.append(file.readlines())
    total+=int(line)
print(list)
print("sum of all elements is:",total)
file.close()


