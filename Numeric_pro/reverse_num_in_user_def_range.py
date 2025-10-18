def reverseNumber(n):
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
    return rev

sr = int(input("Enter a start range :"))
er = int(input("Enter a end range :"))

if sr > er:
    print("Invalid range !!!")
else:
    for i in range(sr,er+1):
        ans = reverseNumber(i)
        print(f"The reversal of {i} is {ans}")

