def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
    print("Leaving fun1")

def fun2():
    print("Entering fun2")
    try:
        res = 10/0
        print("The result is :",res)
    except Exception as e:
        print("Error in fun 2")
    print("Leaving fun2")

print("Program started")
fun1()
print("Program Terminated")