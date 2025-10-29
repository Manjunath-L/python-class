def fun1():
    print("Inside fun1")
def fun2():
    print("Inside fun2")
def disp(ptr1,ptr2):
    print(ptr1)
    print(ptr2)
    ptr1()
    ptr2()

print(fun1)
print(fun2)
ptr3=fun1
ptr4=fun2
print(ptr3)
print(ptr4)
disp(ptr3,ptr4)
