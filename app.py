class Hero:
    def __init__(self):
        self.name = "sudeep"
        self.age = 52
        self.mob = 99887
        self.add = "JPnagur"

    def sing(self):
        print("hero is singing")
    def act(self):
        print("hero is acting")
    def dance(self):
        print("hero is dancing")

h1 = Hero()
print(h1.name)
print(h1.age)
print(h1.mob)
print(h1.add)

#modifing
h1.name = "sudeepa"
h1.mob = 987654

#adding
h1.height = 6.1
h1.noOfMovice = 40

h2 = h1
h3 = h2

print(h3.name)
print(h2.age)
print(h1.mob)
print(h3.add)
print(h2.height)
print(h3.noOfMovice)

h1.sing()
h2.act()
h3.dance()