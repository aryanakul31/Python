import math
cube= lambda a:math.pow(a,3)
power_4= lambda a:cube(a)*a
sq_root= lambda a: math.sqrt(a)

number= int(input('Enter number: '))
print(cube(number))
print(power_4(number))
print(sq_root(number))
