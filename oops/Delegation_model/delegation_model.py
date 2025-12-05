class Radio:
    def turnon(self,x):
        if x == 1:
            print("Radio is on")
        else:
            print("Radio is off")

class Car:
    def __init__(self,min,max):
        self.min = min
        self.max = max
        self.r = Radio()

c1 = Car(10,20)
print(c1.max)
print(c1.min)
c1.r.turnon(1)
c1.r.turnon(2)