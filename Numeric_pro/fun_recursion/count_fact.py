def count_fact(n,i,count):
    if i > n :
        return count
    if n % i == 0:
        count += 1
    return count_fact(n,i+1,count)

n = int(input("Enter a number :"))
count_factors=count_fact(n,1,0)
print(count_factors)