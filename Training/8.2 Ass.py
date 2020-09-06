import math
a_x= int(input('Enter Value of X for Point A: '))
a_y= int(input('Enter Value of Y for Point A: '))
b_x= int(input('Enter Value of X for Point B: '))
b_y= int(input('Enter Value of Y for Point B: '))

distance = math.pow( ( math.fabs(a_x - b_x)**2 + math.fabs(a_y - b_y)**2 ),0.5)
print(distance)
