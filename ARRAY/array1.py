def createintarr():
    l1 = []
    while True:
        try:
            n =int(input("Enter a num :"))
            l1.append(n)
        except Exception as e:
            return l1

print("Enter the ele's to be stored in an array ")
arr = createintarr()
print("Integer array :",arr)