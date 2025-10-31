n = int(input("number :"))

for i in range(1,n+1):
    for j in range(1,i+1  ):
        print("*",end=" ")
    print()

print("=======================")

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("===============================")

for i in range(1,n+1):
    for k in range(n,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("================================")

odd = 1
for i in range(1,(n+1)):
    for k in range(((n*2)-1),odd,-1):
        print(" ",end=" ")
    for j in range(1,(odd+1)):
        print("*",end=" ")
    print()
    odd = odd + 2

print("=================================")

odd1 = 1
for i in range(1,(n+1)):
    for k in range(((n*2)-1),odd1,-1):
        print(" ",end=" ")
    for j in range(1,(odd1+1)):
        print("* ",end=" ")
    print()
    odd1 = odd1 + 2