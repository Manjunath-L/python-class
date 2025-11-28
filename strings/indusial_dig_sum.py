def sumofstr(s1):
    sum = 0
    newstr = ""

    for i in range(0,len(s1)):
        if "0" <= s1[i] <= "9":
            sum += (ord(s1[i])-48)
        else:
            newstr += s1[i]

    newsum = ""
    while sum > 0:
        rem = sum % 10
        newsum = chr(48 + rem) + newsum
        sum = sum // 10
    return newstr+newsum

s1 = str(input("Enter a string :"))
res = sumofstr(s1)
print("the sum of digits in str is :",res)