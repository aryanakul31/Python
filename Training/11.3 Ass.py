user_list= list()
n= int(input('Enter count of numbers to be entered: '))

for i in range(n):
    user_list.append(int(input('Enter item: ')))

for i in user_list:
    if(i%2==0):
        print(i)
