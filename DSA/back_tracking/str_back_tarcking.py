def substr(s,i):
    str = ""
    for j in range(i,len(s)):
        str = str + s[j]
    return str

def remove_str(nstr,orgstr,tarchar):
    if len(orgstr) == 0:
        return nstr

    ch = orgstr[0]
    if ch == tarchar:
        return remove_str(nstr,substr(orgstr,1),tarchar)
    else:
        return  remove_str(nstr + ch,substr(orgstr,1),tarchar)


str = input("Enter a string :")
tar = input("Enter a target element you need to remove :")
res = remove_str("",str,tar)
print(res)