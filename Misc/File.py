# Reading a file
fileRead=open("a.txt","r")
x=fileRead.read()
print(x)

#Writing a file
#Deletes existing data, and enters new one
fileWrite=open("write.txt","w")
fileWrite.write("ink\nPot")
fileWrite.close()

#Writing a file
#This method appends
fileAppend=open("append.txt","a")
fileAppend.write("new")