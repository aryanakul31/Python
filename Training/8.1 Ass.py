import math
entry_list = [0,30,45,60,90]
sin_values = list()
cos_values = list()
tan_values = list()

for i in entry_list:
    rad_value= math.radians(i)
    sin_values.append( math.sin(rad_value) )
    cos_values.append( math.cos(rad_value) )
    tan_values.append( math.tan(rad_value) )

print('Sin:',sin_values)
print('Cos:',cos_values)
print('Tan:',tan_values)
