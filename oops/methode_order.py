# class A:
#     def dispA(self):
#         print("Inside class A")
#
# a = A()
# a.dispA()
# print(A.mro())

# class A:
#     def dispA(self):
#         print("Inside class A")
#
# class B(A):
#     def dispB(self):
#         print("Inside class B")
#
# b = B()
# b.dispB()
# b.dispA()
# print(B.mro())


class A:
    def dispA(self):
        print("Inside class A")

class B:
    def dispB(self):
        print("Inside class B")

class C(A,B):
    def dispC(self):
        print("Inside class C")

c = C()
c.dispC()
c.dispB()
c.dispA()
print(C.mro())
