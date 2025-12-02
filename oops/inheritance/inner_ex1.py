class Cargo:
    def takeoff(self):
        print("Plane is take off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plane is landing")

    def carryc(self):
        print("Plane carry cargo")

class Passenger:
    def takeoff(self):
        print("Plane is take off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plane is landing")

    def carryp(self):
        print("Plane carry passenger")

class Fighter:
    def takeoff(self):
        print("Plane is take off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plane is landing")

    def carryw(self):
        print("Plane carry weapons")

c =Cargo()
p = Passenger()
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