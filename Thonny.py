
def isSameAfterReversals(num):
    return num == 0 or num % 10 != 0

num = int(input("Enter a number :"))
print(isSameAfterReversals(num))