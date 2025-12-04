from abc import abstractmethod,ABC


class Engine(ABC):
    @abstractmethod
    def start(self):...
    @abstractmethod
    def stop(self):...

class Petrolengine(Engine):
    def start(self):
        print("Petrol Engine started")

    def stop(self):
        print("Petrol engine is stopped")

class CNGEngine(Engine):
    def start(self):
        print("CNG engine started")
    def stop(self):
        print("CNG engine stopped")

p = Petrolengine()
c = CNGEngine()
class Car:
    def allow_engine(self,engine:Engine):
        engine.start()
        engine.stop()
c1 = Car()
c1.allow_engine(p)
c1.allow_engine(c)