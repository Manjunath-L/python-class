n = int(input("Enter a number: "))
noc = n
space = 0

for i in range(1, n * 2):
    for k in range(space):
        print("   ", end="")
    for j in range(1, noc + 1):
        print("*", end=" ")
    print()

    if i < n:
        space += 1
        noc -= 1
    else:
        space -= 1
        noc += 1
