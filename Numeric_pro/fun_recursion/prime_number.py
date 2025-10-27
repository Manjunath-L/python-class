def prime_number(n,i=1,count=0):
    if i*i > n:
        return count == 2
    if n % i == 0:
        count = count + 1
        if i != (n//i):
            count = count + 1
    return prime_number(n,i+1,count)

n = int(input("Enter a number :"))
flage = prime_number(n)
if flage:
    print(f"The {n} is prime")
else:
    print(f"The {n} is not prime")




