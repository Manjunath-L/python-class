a=100
def fun1():
    global a
    a = 100
    print(a)
    b=20
    print(b)

def fun2():
    global a
    a = 1000
    print(a)
    c=30
    print(c)

print(a)
print(fun1)
fun2()
print(a)
