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


n = int(input("Enter a num :"))
i = 1
while i * i <= n:
    if n % i == 0:
        print(i,end= " ")
        if i != (n//i):
            print(n//i, end= " ")
    i = i + 1