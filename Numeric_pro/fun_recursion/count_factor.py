def factor_number(n,i=1,count=0):
    if i*i > n:
        return count
    if n % i == 0:
        count = count + 1
        if i != (n//i):
            count = count + 1
    return factor_number(n,i+1,count)

n = int(input("Enter a number :"))
res = factor_number(n)
print(f"The count {n} factor's are : {res}")




