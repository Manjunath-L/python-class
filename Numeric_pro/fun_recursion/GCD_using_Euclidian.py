def GCD_Euc(n1,n2):
    if n1 == 0:
        return n2
    if n1 < n2:
        n1,n2 = n2,n1
    return GCD_Euc((n1%n2),n2)

n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
res = GCD_Euc(n1,n2)
print(res)