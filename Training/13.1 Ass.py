#Inheritance
class Vehicle():
    def __init__(self, tyreCount):
        self.tyreCount= tyreCount

    def printTyreCount(self):
        print(self.tyreCount)

class Bike(Vehicle):
    def __init__(self, tyreCount):
        Vehicle.__init__(self, tyreCount)

obj= Bike(2)
obj.printTyreCount()
