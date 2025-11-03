n = int(input("NUMBER :"))
for i in range(n,(1-1),-1):
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()

print()

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()

print()

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print("",end=" ")
    for j in range(1,(i+1)):
        print("*",end=" ")
    print()
print()

print("#######################Assignement#########")
for i in range(n + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

print()

for i in range(n,(1-1),-1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()

odd = 0
for i in range(1,(n+1)):
    for k in range(((n*2)-1),odd,-1):
        print("*",end=" ")
    for j in range(1,(odd+1)):
        print(" ",end=" ")
    print()
    odd = odd + 2



