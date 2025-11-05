n = int(input("Enter a number:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
print("=================")
for i in range(n,1-1,-1):
    for j in range(i):
        print(i,end=" ")
    print()
print("=================")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("==============")
noc = n
for i in range(1,n*2):
    for j in range(1,noc +1):
        print(j,end=" ")
    print()
    if i >= n:
        noc += 1
    else:
        noc -= 1
print("=============")
for i in range(n,(1-1),-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

