def outer():
    print("Entering outer")
    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")
    print("Calling inner")
    inner()
    print("Leaving outer")
outer()
print("Program Terminated")