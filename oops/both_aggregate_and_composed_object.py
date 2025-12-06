class Heart:
    def __init__(self):
        self.status = True
        print("Heart is ready")

    def getHeart(self):
        print("Heart is waiting")

class Car:
    def __init__(self,name):
        self.cname = name
        print("Car is ready")

    def getCar(self):
        print("Car is used for driving")

class Person:
    def __init__(self,name):
        self.pname=name
        self.c1 = " "
        self.h = Heart()
        print("Person is ready")

    def hasPerson(self,x):
        self.c1 = x
        print("Person is using car for long drive")

p = Person("Modi")
c2 = Car("Nano")
p.hasPerson(c2)
print(p.pname)
print(p.h.status)
print(p.c1.cname)
p.h.getHeart()
p.c1.getCar()
del p
# print(p.pname)
# print(p.h.status)
# print(p.c1.cname)
# p.h.getHeart()
# p.c1.getCar()
print(c2.cname)
c2.getCar()