import json

x='{"name":"alex","age":120,"job":"developer"}'
y=json.dumps(x)
z=json.loads(x)
print(y)
print(z["name"])