setA={1,2,3,4,5,'c','d'}
setB={'a','b','c','d','e',2,3}
union=set()
intersection=set()
difference=set()

for i in setA:
    union.add(i)
for i in setB:
    union.add(i)

for i in setA:
    if i in setB:
        intersection.add(i)

for i in setA:
    if i not in setB:
        difference.add(i)
for i in setB:
    if i not in setA:
        difference.add(i)

print('Set A',setA)
print('Set B',setB)
print('Union',union)
print('Intersection',intersection)
print('Difference',difference)
