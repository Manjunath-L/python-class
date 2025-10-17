# class Demo:
#     def swapcase(self,x,y):
#         temp = x
#         x = y
#         y = temp
#         return [x,y]
#
# d1=Demo()
# a=10
# b=20
# a,b = d1.swapcase(a,b)
# print(a,b)
#
# class cal:
#     def arth_oper(self,a,b):
#         add = a+b
#         sub = a-b
#         mul = a*b
#         div = a/b
#         return [add,sub,mul,div]
#
# c1=cal()
# x=20
# y=10
# [x1,x2,x3,x4] = c1.arth_oper(x,y)
# print(f"{x1}\n{x2}\n{x3}\n{x4}\n")

class Demo:
    x =11
    def __init__(self):
        self.y = 22
        self.z = 33
    def instance_method(self):
        print(self.y)
        print(self.z)
    @staticmethod
    def static_methode():
        print(Demo.x)
    @classmethod
    def class_mehode(cls):
        print("Python")
Demo.static_methode()
Demo.class_mehode()
d1 = Demo()
d1.instance_method()