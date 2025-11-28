def number_sum(s1):
    s1 += " "
    num = 0
    sum = 0
    nstr = ""
    for i in range(0,len(s1)):
        if "0" <= s1[i] <= "9":
            num = (num*10) +(ord(s1[i])-48)
        else:
            if num != 0:
                sum = sum + num
                num = 0
            if (i+1) != len(s1):
                nstr = nstr + s1[i]

    newsum = " "
    while sum > 0:
        rem = sum % 10
        newsum = chr(48 + rem) + newsum
        sum = sum // 10
    return nstr + newsum

s1 = str(input("enter a string :"))
res = number_sum(s1)
print("after sum of number :",res)