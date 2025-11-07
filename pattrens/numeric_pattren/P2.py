n = int(input("Enter a number :"))
# code 1
for i in range(n,1-1,-1):
    for j in range(i,1-1,-1):
        print(j,end=" ")
    print()
print("=====================")
# code 2
noc = 1
for i in range(1,n*2):
    for j in range(noc,1-1,-1):
        print(j,end=" ")
    print()
    if n > i:
        noc += 1
    else:
        noc -= 1
print("=======================")
# code 3
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j) % 2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
print("=====================")
# code 4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i < j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("======================")
# code 5
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i > j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()
print("========================")
# code 6
count = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(count,end=" ")
        count+= 1
    print()
print("========================")
# code 7
count = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i % 2 != 0:
            print(count,end=" ")
            # collecting the printed val of odd row
            count2 = count
        else:
            print(count2,end=" ")
            count2 -= 1
        count+= 1# increment in continuous no matter
                # i --> odd or even
    print()
    count2 = count2 + n#before going to even row sum
    #collected val+n
print("==========================")
# code 8
noc = n
for i in range(1,n*2):
    for k in range(n,noc,-1):
        print(" ",end=" ")
    for j in range(1,noc+1):
        print(j,end=" ")
    print()
    if i < n:
        noc -= 1
    else:
        noc += 1
print("======================")
# code 9
for i in range(1,n+1):
    for j in range(1,n+1):
        if i > j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
print("======================")
# code 10
for i in range(n,1-1,-1):
    for j in range(n,1-1,-1):
        if i < j:
            print(j,end=" ")
        else:
            print(i,end=" ")
    print()
print("=======================")
# code 11
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        if i % 2 != 0:
            print(count,end=" ")
            # collecting the printed val of odd row
            count2 = count + 1
        else:
            print(count2,end=" ")
            count2 -= 1
        count+= 1# increment in continuous no matter
                # i --> odd or even
    print()
    count2 = count2 + i#before going to even row sum
    #collected val+n

print("============================")
# code 12
count = n
for i in range(1,n+1):
    for j in range(i,count+1):
        print(j,end=" ")
    print()
    count += 1