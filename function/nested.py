def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
outer()
