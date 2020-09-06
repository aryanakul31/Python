#Filter
def filterVowels(alphabet):
    vowels=['a','e','i','o','u']
    if alphabet in vowels:
        return True
    else:
        return False


alphabets=['a','b','c','d','e','f']

vowels= list(filter(filterVowels, alphabets))
print(vowels)
print('\n\n')

#Reduce
import functools
numbersList= [1,2,3,4,5,6,7,8,9]
numbersSum= functools.reduce(lambda a,b:a+b, numbersList)
print('Sum of',numbersList,'is',numbersSum)
maximum= functools.reduce(lambda a,b: a if a>b else b, numbersList)
print('Maximum of',numbersList,'is',maximum)
print('\n\n')

#Map
def square(a):
    return a*a

numbersList= [1,2,3,4,5,6,7,8,9]
map_1= map(square, numbersList)
map_2= map(lambda x: x*x, numbersList)
print('Map 1',list(map_1))
print('Map 2',list(map_2))
print('\n\n')

#Enum
import enum
class Days(enum.Enum):
    Sun= 1
    Mon= 2


print('Enum as string:', Days.Sun)
print('Enum member name:', Days.Sun.name)
print('Enum member value:', Days.Sun.value)
print('Enum using index:', Days(2))
