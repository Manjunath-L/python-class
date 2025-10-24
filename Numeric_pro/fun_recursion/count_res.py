def count_degits(n,count=0):
    if n <= 0:
        return count
    n = n // 10
    count = count +  1
    return count_degits(n,count)

num = int(input("Enter a num :"))
res = count_degits(num)
print(f"the count of digits in {num} is:{res}")