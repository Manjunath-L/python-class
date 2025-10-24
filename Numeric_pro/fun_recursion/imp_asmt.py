def printnum(n, i=1):
    if i > n:
        return
    print(i)
    printnum(n, i + 1)
    print(i)

n = int(input("Enter a number: "))
printnum(n)



