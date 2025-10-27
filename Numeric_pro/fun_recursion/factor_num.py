
def factor_number(n,i=1):
    if i*i > n:
        return
    if n % i == 0:
        print(i)
        if i != (n//i):
            print(n//i)
    return factor_number(n,i+1)

n = int(input("Enter a number :"))
factor_number(n)


