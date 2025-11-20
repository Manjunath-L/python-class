import pickle
class Employee:
    def __init__(self,eid,ename,edes,esal):
        self.eid = eid
        self.ename = ename
        self.edes = edes
        self.esal = esal
    def disp(self):
        print(self.eid)
        print(self.ename)
        print(self.edes)
        print(self.esal)


e = Employee(101,"Rama","dev",25000)
f = open("name.txt","wb")
pickle.dump(e,f)
f.close()
print("Object is stored into the text file")

