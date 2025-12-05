class Charger:
    def __init__(self,name):
        self.cname = name
        print("Charger is ready")

    def getCharger(self):
        print("Charger is used for charging")

class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c1 = " "
        print("Mobile is ready")

    def hasMobile(self,x):
        self.c1 = x
        print("Both mobile and charger connected")

m = Mobile("Samsung")
c2 = Charger("Samsung Charger")

m.hasMobile(c2)
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
del m
print("After deleting")
print(c2.cname)
c2.getCharger()
print(m.mname)
print(m.c1.cname)
m.c1.getCharger()
