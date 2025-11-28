class student:
    def __init__(self):
        self.__name1 = " "
        self.__name2 = " "
    def getter(self):
        return self.__name1
    def setter(self,v):
        self.__name1 = v

    getset = property(getter,setter)

    def getter1(self):
        return  self.__name2
    def setter1(self,v):
        self.__name2 = v

    setget = property(getter1,setter1)

s = student()
s.getset = "Rama"
res = s.getset
print(res)
s.setget = "sita"
print(s.setget)

