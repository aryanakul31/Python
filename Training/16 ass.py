import time
from threading import Thread

class A(Thread):
    def __init__(self):
        Thread.__init__(self,name="fruits")
    def run(self):
        fruits=["apple","mango","grapes"]
        for i in fruits:
            print(i)
            time.sleep(1)

class B(Thread):
    def __init__(self):
        Thread.__init__(self,name="alphabets")
    def run(self):
        alphabets=["a","b","d"]
        for x in alphabets:
            print(x)
            time.sleep(1)

class C(Thread):
    def __init__(self):
        Thread.__init__(self,name="numbers")
    def run(self):
        numbers=["23","4","56"]
        for y in numbers:
            print(y)
            time.sleep(1)
            
obj=A()
obj.start()
#obj.join()

obj1=B()
obj1.start()
#obj1.join()

obj2=C()
obj2.start()
#obj2.join()
