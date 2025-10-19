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
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            count += 1
            if i != (n // i):
                print(n // i, end=" ")
                count += 1
        i = i + 1
    return count

n = int(input("Enter a num :"))
count = factor(n)
print("\n",count)