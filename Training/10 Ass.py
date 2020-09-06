sentence= input('Enter sentence: ')
dictionary= {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for i in sentence:
    if i=='a':
        dictionary['a']+=1
    elif i=='e':
        dictionary['e']+=1
    elif i=='i':
        dictionary['i']+=1
    elif i=='o':
        dictionary['o']+=1
    elif i=='u':
        dictionary['u']+=1

print(dictionary)
