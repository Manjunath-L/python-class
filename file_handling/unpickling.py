import pickle
class Employee:
    def __init__(self,eid,ename,edes,esal):
        self.eid = eid
        self.ename = ename
        self.edes = edes
        self.esal = esal
    def display(self):
        print(self.eid)
        print(self.ename)
        print(self.edes)
        print(self.esal)
f = open("name.txt","rb")
e = pickle.load(f)
e.display()
print("object retrieved")
f.close()