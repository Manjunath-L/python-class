n = int(input("Enter a number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == 1 or j == n or i + j == n + 1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()