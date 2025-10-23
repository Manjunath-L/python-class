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

n = int(input("Enter a rnange :"))
count = 0
while n > 0:
    flage 