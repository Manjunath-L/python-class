# def count_factor(n):
#     count = 0
#     countCycle = 0
#     print(f"The factors of {n} are :")
#     for i in range(1,n+1):
#         if n % i ==0:
#             count = count + 1
#         countCycle = countCycle + 1
#     return count,countCycle
#
# n = int(input("Enter a number :"))
# res,ans = count_factor(n)
# print(res)
# print(f"The count of cycle is {ans}.")

def factor(n):
    i = 1
    count = 0
    count_factror = 0
    while i * i <= n:
        count += 1
        if n % i == 0:
            print(i, end=" ")
            count_factror += 1
            if i != (n // i):
                print(n // i, end=" ")
                count_factror += 1
        i = i + 1
    return [count,count_factror]

n = int(input("Enter a num :"))
a,b=factor(n)
print(f"\ncount cycle : {a}")
print(f"count fact : {b}")