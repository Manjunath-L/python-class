def reverse_str(s):
    new = ""
    for i in range(0,len(s)):
        new = s[i] + new
    return new

def reverse_str2(s):
    new = ""
    for i in range(len(s)-1,0-1,-1):
        new = new + s[i]
    return new

def reverse_str3(s,i,nstr):
    if i == len(s):
        return nstr
    nstr = s[i] + nstr
    return reverse_str3(s,i+1,nstr)

def reverse_str4(s,i,nstr):
    if i < 0:
        return nstr
    nstr += s[i]
    return reverse_str4(s,i-1,nstr)

s = str(input("Enter a string :"))
rev = reverse_str(s)
rev1 = reverse_str2(s)
res = reverse_str3(s,0,"")
res1 = reverse_str4(s,len(s)-1,"")
print(res1)
print(res)
print(rev)
print(rev1)
