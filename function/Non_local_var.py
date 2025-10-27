# def fun1():
#     a = 10 #Non-local varible
#     print("From fun 1 a :",a)
#     def fun2():
#         b = 20
#         print("from fun2 b ",b)
#         print("form fun 2 a" ,a)
#     fun2()
#     print("form fun1 a",a)
#     print("form fun1 b",b)
# fun1()


# def fun1():
#     a = 10 #Non-local variable
#     print("From fun 1 a :",a)
#     def fun2():
#         nonlocal a
#         a = 100
#         b = 20
#         print("from fun2 b ",b)
#         print("form fun 2 a" ,a)
#     fun2()
#     print("form fun1 a",a)
# fun1()


def fun1():
    a =100
    print("Before a ",a)
    def fun2():
        nonlocal a
        a = 999
        b =200
        print(a)
        print(b)
    fun2()
    print("After a",a)
fun1()
