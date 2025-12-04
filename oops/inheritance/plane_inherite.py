from plane import *
class Plane:
    def takeoff(self):
        print("Plane is take off")

    def fly(self):
        print("Plane is flying")

    def land(self):
#         print("Plane is landing")
class cargo(Plane):
    def carryc(self):
        print("Plane carry cargo")

class passenger(Plane):
    def carryp(self):
        print("Plane carry passenger")

class Fighter(Plane):
    def carryw(self):
        print("Plane carry weapons")

c =cargo()
p = passenger()
f = Fighter()

c.takeoff()
c.fly()
c.land()
c.carryc()
p.takeoff()
p.fly()
p.land()
p.carryp()
f.takeoff()
f.fly()
f.land()
f.carryw()