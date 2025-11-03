n = int(input("Number :"))
noc1 = 1
for i in range(1,(n*2)):
    for k in range(n*2,noc1,-1):
        print("",end=" ")
    for j in range(1,noc1+1):
        print("*",end=" ")
    print()
    if i < n:
        noc1 += 1
    else:
        noc1 -= 1