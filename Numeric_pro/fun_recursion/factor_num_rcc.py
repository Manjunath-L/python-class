def is_fact(n,i=1):
    if i > n :
        return
    if n % i == 0:
        print(i)
    return is_fact(n,i+1)

n = int(input("Enter a number :"))
is_fact(n)