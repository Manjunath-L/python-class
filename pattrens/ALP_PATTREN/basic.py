n = int(input("number :"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(96+i),end=" ")
    print()
print("=========================")
for i in range(n,1-1,-1):
    for j in range(1,i+1):
        if i %2 == 0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print()
print("=============================")
for i in range(1,n+1):
    for j in range(n,i-1,-1):
       print(chr(96+j),end=" ")
    print()
print("=============================")
for i in range(n,1-1,-1):
    for j in range(i,1-1,-1):
        print(chr(64+j),end=" ")
    print()
print("===========================")
noc = 1
for i in range(1,n*2):
    for j in range(n,noc-1,-1):
        print(chr(96+j),end=" ")
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1
print("=============================")
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j) % 2 == 0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+2),end=" ")
    print()
print("===========================")
for i in range(1,n+1):
    count = n
    for j in range(1,n+1):
        if i % 2 != 0:
            print(chr(64+j),end=" ")
        else:
            print(chr(96+count),end=" ")
            count -= 1
    print()
