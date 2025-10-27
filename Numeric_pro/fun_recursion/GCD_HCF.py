def Gcd_number(n1,n2,lower,i,hcf):
    if i > lower:
        return hcf
    if n1 % i == 0 and n2 % i == 0:
        hcf = i
    return Gcd_number(n1,n2,lower,i+1,hcf)

n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number2 :"))
lower = n1
if n2 < n1:
    lower = n2
hcf = 1
res = Gcd_number(n1,n2,lower,2,hcf)
print(res)