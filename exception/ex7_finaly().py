def fun1():
    print("Function1 connected to db")
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    finally:
        print("Fun1 closing DB")

def fun2():
    print("Fun2 connected to db")
    try:
        res = 10 / 2
        print("The result is :",res)
    except Exception as e:
        print("Error in fun2")
        raise e
    finally:
        print("Fun2 closeing DB")

print("Program started")
try:
    fun1()
except Exception as e:
    print("Error is main")
print("Program Terminated")