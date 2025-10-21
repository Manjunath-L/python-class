# def prime_num(n):
#     if n < 0:
#         if n == 1:
#             return False
#         if n == 2:
#             return True
#         for i in range(2,int(n/2)+1):
#             if n % i == 0:
#                 return False
#     return True

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

n = int(input("Enter a number :"))
flage = prime_num(n)
if flage:
    print(f"prime number : {n}")
else:
    print(f"not a prime number : {n}")
