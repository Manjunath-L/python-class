l = [10,20,30,40]
print(l)
print(len(l))
l1 = ["rama",22,2.3,True]
print(l1)
print(type(l1))
l2 = [10,20,10,20,30]
print(l2)
l3=[]
print(l3)

a = [[],]
i = 0
while True:
    data = int(input("Enter a number :"))
    a.insert(i,data)
    i = i+1
    print("Do you wish to continue")
    choice = int(input("press 1: yes\n press 2: no"))
    if choice == 1:
        continue
    else:
        break
print(a)