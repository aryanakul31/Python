n= int(input('Enter number Fibonacci Series: '))
first_number= 0
second_number= 1
print(first_number,second_number,end=' ')
for i in range(2, n):
    third_number= first_number+second_number
    print(third_number, end=' ')
    first_number= second_number
    second_number= third_number
