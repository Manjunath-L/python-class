a = 10
def fun1():
    global a
    a = 100
    b = 20
    print(a)
    print(b)
    def fun2():
        global a
        nonlocal b
        a = 1000
        b = 200
        c = 30
        print(a)
        print(b)
        print(c)
    fun2()
    print(a)
fun1()

class Demo:
    x = 11
    def __init__(self):
        self.y = 22
        self.z = 33

    def display(self):
        print(self.y)
        print(self.z)
        a = 10
        b = 20
        c = a + b
        print(c)

d1 = Demo()
print(Demo.x)
d1.display()
print(a)