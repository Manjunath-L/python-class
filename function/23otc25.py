def fun1():
    print("Invoking fun1")
def fun2(a,b):
    c=a+b
    print("the sum is",c)


def display(ptr1,ptr2):
    ptr1()
    x=40
    y=40
    ptr2(x,y)


fun1()
x=40
y=9090
fun2(x,y)
ptr1=fun1
ptr2=fun2
ptr1()
display(ptr1,ptr2)
ptr2(100,200)
print(fun1)
print(ptr1)
print(fun2)
print(ptr2)