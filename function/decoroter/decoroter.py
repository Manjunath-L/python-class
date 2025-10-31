def print_msg():
    msg = "Hello Everyone"
    return msg
def outer(print1):
    print("Entering outer")
    def inner():
        print("Entering inner")
        res1 = print1
        msg2 = res1()
        new_v = msg2.upper()
        print(new_v)
        print("Leaving inner")
    return inner
ptr1 = outer(print_msg)
ptr1()