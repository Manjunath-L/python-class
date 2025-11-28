def strfilter(s):
    newstr = ""
    for i in range(0,len(s)):
        if "A" <= s[i] <= "Z":
            newstr = newstr + chr(ord(s[i]) + 32)
        elif ("a" <= s[i] <= "z") or ("0" <= s[i] <= "9"):
            newstr = newstr + s[i]
    return  newstr

def checkpall(s):
    s = strfilter(s)
    i ,j = 0,len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True



s = str(input("Enter a string :"))
flage = checkpall(s)
if flage:
    print(f"The given str is pallandrom {s}")
else:
    print(f"The given str in not pallandrom {s}")