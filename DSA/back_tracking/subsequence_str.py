def substr(s,i):
    str = ""
    for j in range(i,len(s)):
        str = str + s[j]
    return str

def sub_sequence(nstr,orgstr):
    if len(orgstr) == 0:
        print(nstr)
        return
    ch = orgstr[0]
    sub_sequence(nstr+ch,substr(orgstr,1))
    sub_sequence(nstr,substr(orgstr,1))

str = input("Enter a string :")
sub_sequence("",str)