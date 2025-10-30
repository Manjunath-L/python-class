def print_mesg():
    print("Hello Everyone")
def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering inner")
        res = print1
        res()
        print("Leaving inner")
    return inner
ptr1 = print_mesg
ptr2 = outer(ptr1)
print("After calling outer")
ptr2()
print("After calling inner using ptr2")