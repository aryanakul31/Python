marks= int(input('Enter your marks: '))
if(marks>100):
    print('Please enter correct marks')
elif(marks>=90):
    print('Grade A')
elif(marks>=80):
    print('Grade B')
elif(marks>=60):
    print('Grade C')
elif(marks>=50):
    print('Grade D')
elif(marks<50):
    print('Grade E')
