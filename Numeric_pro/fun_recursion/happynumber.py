def happynum(n):
    if n == 1:
        return True
    elif n == 4:
        return False
    sum = 0
    while n > 0:
        base = n% 10
        sum = sum + (base**2)
        n = n// 10
    return happynum(sum)

n = int(input("Enter a number :"))
flage = happynum(n)
if flage:
    print("Happy Number")
else:
    print("Not a Happy Number")