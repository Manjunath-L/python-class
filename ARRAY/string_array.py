def createstrarray():
    l1 = []
    while True:
        n = input("Enter num: ")
        if n == "":
            return l1
        l1.append(n)
print("Enter the ele's to store in the array:")
arr = createstrarray()
print("string present in array :",arr)

print("================================")

def createstrarray1():
    l1 = []
    while True:
        n = input("Enter num: ")
        if n == "":
            return l1
        l1.append(n[0])
print("Enter the ele's to store in the array:")
arr = createstrarray1()
print("string present in array :",arr)