a = int(input("Enter the value1 :"))
b = int(input("Enter the value2 :"))
try:
    c = a/b
    print("The result is :",c)
except Exception as e:
    print("error")
print("program ended")