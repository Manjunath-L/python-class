def sum_of_num(n,sum):
    if n <= 0:
        return sum
    m = n %10
    sum = sum + m
    n = n//10
    return sum_of_num(n,sum)

n = int(input("Enter a number :"))
res = sum_of_num(n,0)
print(res)