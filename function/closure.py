def outer():
    print("Inside outer")
    def inner():
        print(f"Inside {inner}")
    return inner
ref=outer()
print(ref)
ref()