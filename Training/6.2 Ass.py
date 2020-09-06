n= int(input('Enter number :'))
sum=0
count=0
for i in range(1, n+1):
    if i%7==0 :
        print(i)
        sum+=i
        count+=1

avg= sum/count
print('\n\nSum ',sum)
print('Numbers ',count)
print('Avg ',avg)
