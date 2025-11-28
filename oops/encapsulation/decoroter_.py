class student:
    def __init__(self):
        self.__name = ""

    @property
    def dataAccess(self):
        return self.__name

    @dataAccess.setter
    def dataAccess(self,v):
        self.__name = v

s = student()
s.dataAccess = "Rama"
res1 = s.dataAccess
print(res1)