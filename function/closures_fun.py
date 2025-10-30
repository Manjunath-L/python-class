def outer():
    print("Entering outer")
    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")
    return inner
res = outer()
print("After calling outer")
res()
print("After calling inner using res")

