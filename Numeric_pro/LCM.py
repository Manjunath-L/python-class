n1 = int(input("Enter a number :"))
n2 = int(input("Enter a number :"))

def LCM(n1,n2):
    lcm = n1
    if n1 < n2:
        lcm = n2
    while True:
        if lcm % n1 == 0 and lcm % n2 == 0:
            return lcm
        lcm += 1

print(LCM(n1,n2))