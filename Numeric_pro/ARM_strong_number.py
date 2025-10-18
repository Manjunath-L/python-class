def countdigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

def ARM_number(n):
    temp = n
    if n < 0:
        n = n * (-1)
    power = countdigits(n)
    ans = 0
    while n > 0:
        base = n % 10
        ans = ans + (base ** power)
        n = n // 10
    if temp < 0:
        ans = ans*(-1)
    return ans == temp

n = int(input("Enter a digit :"))
flage = ARM_number(n)
if  flage:
    print(f"{n} is ARM strong number")
else:
    print(f"{n} is Not ARM strong number")