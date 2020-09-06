number_1= int(input('Enter 1st number: '))
number_2= int(input('Enter 2nd number: '))
number_3= int(input('Enter 3rd number: '))
max= 0
if number_1>=number_2:
    if number_1>number_3:
        max= number_1
    elif number_1<number_3:
        max= number_3
    elif number_1==number_3:
        max=0

elif number_2>number_1:
    if number_2>number_3:
        max= number_2
    elif number_2<number_3:
        max= number_3
    elif number_2==number_3:
        max=0

if max ==0:
    print('All three numbers are equal')
else:
    print('Max number is', max)
