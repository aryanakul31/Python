numbers= list()
for i in range(1,11):
    numbers.append(int(input('Enter Number :')))

numbers.sort()

print('Sum:', sum(numbers))
print('Max:', max(numbers))
print('Min:', min(numbers))
median= sum( numbers[int(len(numbers)/2)-1:int(len(numbers)/2)+1] )/2
print('Median:',median)
print('Square:',end=' ')
for i in numbers:
    print(i*i,end=' ')
print('\nCube:',end=' ')
for i in numbers:
    print(i*i*i,end=' ')
