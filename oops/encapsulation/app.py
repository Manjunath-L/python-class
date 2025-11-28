class Book:
    def __init__(self,values):
        self.pages = values
b =Book(100)
print(b.pages)
b.pages = 114
print(b.pages)
b.pages = -99
print(b.pages)

class Book:
    def __init__(self,values):
        self.__pages = values
    def setter_rrtyui(self,values):
        if (values > 0):
            self.__pages = values
    def getter(self):
        return self.__pages
b = Book(100)
b = Book(99)
# b.setter(114)
res = b.getter()
print(res)
b.setter_rrtyui(-99)
print(b.getter())

class Persone:
    def __init__(self):
        self.__name = " "
    def getter(self):
        return self.__name
    def metter(self,value):
        self.__name = value

p = Persone()
p.metter("Rama")
res = p.getter()
print(res)
print(p.getter())