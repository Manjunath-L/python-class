n1 = int(input("Enter a num 1 :"))
n2 = int(input("Enter a num 2 :"))
lower =  n1
if n2 < n1:
    lower = n2
hcf = 1

for i in range(2,lower+1):
    if n1 % i ==0 and n2 % i == 0:
        hcf = i

print(hcf)
