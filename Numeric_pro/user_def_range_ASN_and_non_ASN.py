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

sr = int(input("Enter a start value :"))
er = int(input("Enter a end value :"))

if sr > er:
    print("Invalid range !!")
else:
    print("ASN Numbers")
    for i in range(sr,er+1):
        ans = ARM_number(i)
        if ans:
            print(i,end=" ")
    print("\nNon-ASM Numbers")
    for i in range(sr,er+1):
        ans = ARM_number(i)
        if not ans:
            print(i,end=" ")