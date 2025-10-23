def prime_num(n):
    count_fact = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count_fact += 1
            if i != (n//2):
                count_fact += 1
        i = i+ 1

    return count_fact == 2

sr = int(input("Enter a start number :"))
er = int(input("Enter a end number :"))
for i in range(sr,er+1):
    flage = prime_num(i)
    if flage:
        print(f"prime number : {i}")
    else:
        print(f"not a prime number : {i}")