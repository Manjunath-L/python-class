n = int(input("Enter a number :"))

noc1 = 1
for i in range(1,(n*2)):
    for k in range(n*2-1,noc1,-1):
        print("",end=" ")
    for j in range(1,noc1+1):
        print("*",end=" ")
    print()
    if i < n:
        noc1 += 2
    else:
        noc1 -= 2