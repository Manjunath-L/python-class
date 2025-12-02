class Plane:
    def takeoff(self):
        print("Plane is take off")

    def fly(self):
        print("Plane is flying")

    def land(self):
        print("Plane is landing")

class Cargo(Plane):
    def takeoff(self):
        print("Cargo is take off")

    def fly(self):
        print("Cargo is flying")

    def land(self):
        print("Cargo is landing")

class Passenger(Plane):
    def takeoff(self):
        print("Passenger is take off")

    def fly(self):
        print("Passenger is flying")

    def land(self):
        print("Passenger is landing")

class Fighter(Plane):
    def takeoff(self):
        print("Fighter is take off")

    def fly(self):
        print("Fighter is flying")

    def land(self):
        print("Fighter is landing")

c =Cargo()
p = Passenger()
f = Fighter()

def allowPlane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()

allowPlane(c)
allowPlane(p)
allowPlane(f)