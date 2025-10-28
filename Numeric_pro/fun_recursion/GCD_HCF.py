def GCD_num(n1,n2,i,lower,hcf):
    if n2 < n1:
        lower = n2
    if i > lower:
        return hcf
    if n1 % i == 0 and n2 % i == 0:
        hcf = i
    return GCD_num(n1,n2,(i+1),lower,hcf)

n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))
lower  = n1
hcf  = 1
res = GCD_num(n1,n2,2,lower,hcf)
print(res)
