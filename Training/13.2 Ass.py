# Access Specifiers
class Parent:
    
    var1= None #Public variable
    _var2= None #Protected Variable
    __var= None #Private Variable

    def __init__(self, var1, var2, var3):
        self.var1= var1
        self._var2= var2
        self.__var3= var3

    def displayPublicMembers(self): #Public Function
        print("Public Variable:",self.var1)

    def _displayProtectedMembers(self): #Protected Function
        print("Protected Variable:",self._var2)

    def __displayPrivateMembers(self):  #Private Function
        print("Private Variable:",self.__var3)


    def accessPrivateFunction(self):
        self.__displayPrivateMembers()

class Child(Parent):
    
    def __init__(self, var1, var2, var3):
        Parent.__init__(self, var1, var2, var3)

    def accessProtectedFunction(self):
        self._displayProtectedMembers()

obj= Child(1, 2, 3)
obj.displayPublicMembers()
obj.accessProtectedFunction()
obj.accessPrivateFunction()

print("Protected Member Using Object:",obj._var2)
