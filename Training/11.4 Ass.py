def filtering_divisble(number):
    if number==0:
        return False
    elif number%7==0:
        return True
    else:
        return False


count= int(input('Enter count of numbers: '))
user_list= list()

for i in range(count):
    user_list.append(int(input('Enter number: ')))

filtered_numbers= filter(filtering_divisble, user_list)
print('Numbers divisible by 7 are: ', end=' ')
for i in filtered_numbers:
    print(i, end=' ')
