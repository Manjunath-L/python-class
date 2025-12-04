from abc import ABC, abstractmethod


class Plane(ABC):
    @abstractmethod
    def takeoff(self):...
    @abstractmethod
    def fly(self):...
    @abstractmethod
    def land(self):...

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

def allowPlane(ref:Plane):
    ref.takeoff()
    ref.fly()
    ref.land()

allowPlane(Cargo())
allowPlane(Passenger())
allowPlane(Fighter())