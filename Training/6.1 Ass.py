a= ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']
strings_list= list()
s_count=0
numbers_list= list()
n_count=0

for i in a:
    if isinstance(i,str):
        strings_list.insert(s_count, i)
    else:
        numbers_list.insert(n_count, i)

print('Strings List Ascending Order')
strings_list.sort()
for x in strings_list:
    print(x)
print('\nStrings List Descending Order')
strings_list.sort(reverse= True)
for x in strings_list:
    print(x)

    
print('\n\nNumbers List Ascening Order')
numbers_list.sort()
for y in  numbers_list:
    print(y)
print('\nNumbers List Descending Order')
numbers_list.sort(reverse=True)
for y in numbers_list:
    print(y)
