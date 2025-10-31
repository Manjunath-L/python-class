def outer(fun1):
    def inner():
        print("Entering inner")
        ret1 = fun1()
        ret2 = ret1[::-1]
        print(ret2)
        print("Leaving inner")
    return inner
@outer   # print_msg = outer(print_msg)
def print_mas():
    str1="Pentagon space"
    return str1
print_mas()
@outer
def print2():
    str1="space"
    return str1
print2()