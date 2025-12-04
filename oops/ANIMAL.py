class Animal:
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

    def breath(self):
        print("Animal is breath")

class Tiger(Animal):
    def eat(self):
        print("Tiger is eating")

    def sleep(self):
        print("Tiger is sleeping")

    def breath(self):
        print("Tiger is breath")

class Deer(Animal):
    def eat(self):
        print("Deer is eating")

    def sleep(self):
        print("Deer is sleeping")

    def breath(self):
        print("Deer is breath")

class Monkey(Animal):
    def eat(self):
        print("Monkey is take off")

    def sleep(self):
        print("Monkey is flying")

    def breath(self):
        print("Monkey is landing")

t = Tiger()
d = Deer()
m = Monkey()

def allowanimals(ref):
    ref.eat()
    ref.sleep()
    ref.breath()

allowanimals(t)
allowanimals(d)
allowanimals(m)
