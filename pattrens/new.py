n = int(input("number :"))
for i in range(1,n+1):
    for k in range(0,i+1):
        print(" ",end=" ")
    for j in range(1,n+1):
        print("*",end=" ")
    print()

for i in range(1,n+1):
    for k in range(0,i-1):
        print(" ",end=" ")
    for j in range(1,n+1):
        if i == 1 or j == 1 or i == n or j == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()