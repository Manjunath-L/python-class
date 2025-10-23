def fibo_ser(pos):
    n1,n2 = 0,1
    temp = 1
    #decrement loop
    # while pos > 0:
    #     print(n1,end=" ")
    #     temp = n1 + n2
    #     n1 = n2
    #     n2 = temp
    #     pos -= 1
    #increment loop
    # i = 1
    # while i <= pos:
    #     print(n1, end=" ")
    #     temp = n1 + n2
    #     n1 = n2
    #     n2 = temp
    #     i = i + 1
    #decrement
    for i in range(pos,0,-1):
        print(n1,end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp
    #increment
    # for i in range(1,(pos+1)):
    #     print(n1,end=" ")
    #     temp = n1 + n2
    #     n1 = n2
    #     n2 = temp
pos = int(input("Enter a position :"))
fibo_ser(pos)
