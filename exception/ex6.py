# Hndling specific exception
try:
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    c = a/b
    print("The result is :",c)
except ValueError as e:
    print("Value error")
    print(e)
    print(str(e))
    print(e.__str__())
except ZeroDivisionError as e:
    print("Value error")
    print(e)
    print(str(e))
    print(e.__str__())
except Exception as e:
    print("Value error")
    print(e)
    print(str(e))
    print(e.__str__())
print("Program Terminated")
