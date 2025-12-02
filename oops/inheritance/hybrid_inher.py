class A:
    def dispA(self):
        print("Inside dispA")

class B(A):
    def dispB(self):
        print("Inside dispB")

class C(A):
    def dispC(self):
        print("Inside dispc")

class D(B,C):
    def dispD(self):
        print("Inside dispC")


d1 =D()
d1.dispA()
d1.dispB()
d1.dispC()
d1.dispD()