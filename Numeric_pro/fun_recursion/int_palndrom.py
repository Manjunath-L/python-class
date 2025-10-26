def int_pal(n,rev,temp):
    if n <= 0:
        return rev == temp
    rem = n % 10
    rev = (rev * 10)+rem
    n = n//10
    return int_pal(n,rev,temp)

n = int(input("Enter a number :"))
flage = int_pal(n,0,n)
if flage:
    print(f"{n} is palindrome ")
else:
    print(f"{n} is not palindrome")
