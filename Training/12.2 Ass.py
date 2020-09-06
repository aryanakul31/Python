class Employee:
    """
    This is my documentation
    """
    def __init__(self, eid, name, age):
        self.eid= eid
        self.name= name
        self.age= age

    def __str__(self):
        return self.name

obj= Employee(1, 'Nakul', 21)
print(obj)
print(obj.__doc__)
print(obj.__dict__)
print(obj.__module__)
