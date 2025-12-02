class A:
    def dispA(self):
        print("Inside dispA")

class B:
    def dispB(self):
        print("Inside dispB")

class c(A,B):
    def dispC(self):
        print("Inside dispc")

c1 = c()
c1.dispC()
c1.dispB()
c1.dispA()