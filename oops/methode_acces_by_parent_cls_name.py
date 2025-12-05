class A:
    def display(self):
        print("Inside class A")

class B(A):
    def display(self):
        A.display(self)
        print("Inside class B")

class C(B):
    def display(self):
        B.display(self)
        print("Inside class C")

class D(C):
    def display(self):
        C.display(self)
        print("Inside class D")


d1 = D()
d1.display()
