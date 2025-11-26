def alpsmallcase(s1):
    newstr = ""
    i = 0
    while i < len(s1):
        if "A" <= s1[i] <= "Z":
            newstr += chr(ord(s1[i]) + 32)
            i += 1
        else:
            newstr += s1[i]
            i += 1
    return newstr

def alpscaptilalcase(s1):
    newstr = ""
    for i in range(len(s1)):
        if "a" <= s1[i] <= "z":
            newstr += chr(ord(s1[i]) - 32)
        else:
            newstr += s1[i]
    return newstr

def alpswapcase(s1):
    newstr = ""
    for i in range(len(s1)):
        if "a" <= s1[i] <= "z":
            newstr += chr(ord(s1[i]) - 32)
        elif "A" <= s1[i] <= "Z":
            newstr += chr(ord(s1[i]) + 32)
        else:
            newstr += s1[i]
    return newstr

s1 = str(input("Enter a string : "))
res = alpsmallcase(s1)
res2 = alpscaptilalcase(s1)
res3 = alpswapcase(s1)
print("After converting to small case :",res)
print("After converting to capital case :",res2)
print("After converting to swap case :",res3)