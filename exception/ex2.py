a = int(input("Enter the value1 :"))
b = int(input("Enter the value2 :"))
try:
    c = a/b
except Exception as e:
    print("error")
else:
    print("The result is :",c)
    print("no error found")
print("program ended")