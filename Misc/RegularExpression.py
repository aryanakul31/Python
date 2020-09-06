import re

msg = 'Call 415-555-1011 tomorrow, 415-555-9999'
phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
number = phoneNumber.findall(msg)
print(number)