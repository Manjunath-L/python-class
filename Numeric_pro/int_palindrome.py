def countdigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

def Palindrome(n):
    temp = n
    if n < 0:
        n = n * (-1)
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10 ) + rem
        n = n // 10
    if temp < 0:
        rev = rev * (-1)
    return rev == temp

val = int(input("Enter a number: "))
flage = Palindrome(val)
if flage:
    print(f"{val} is Palindrome")
else:
    print(f"{val} is Not Palindrome")