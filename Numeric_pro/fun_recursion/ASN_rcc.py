def count_degits(n,count=0):
    if n <= 0:
        return count
    n = n // 10
    count = count +  1
    return count_degits(n,count)

def ASN_num(n,power,asn,temp):
    if n <= 0:
        return temp == asn
    base = n % 10
    asn = asn + (base ** power)
    n= n // 10
    return ASN_num(n,power,asn,temp)

n = int(input("Enter a number :"))
pow = count_degits(n)
flage = ASN_num(n,pow,0,n)
if flage:
    print(f"{n} is ASN ")
else:
    print(f"{n} is not a ASN ")