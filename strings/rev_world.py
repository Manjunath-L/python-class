def rev_world(s):
    s = s + " "
    i = 0
    newr = ""
    nest = ""
    # while i < len(s):
    #     if s[i] != " ":
    #         newr = s[i] + newr
    #     elif newr != "":
    #         if nest == "":
    #             nest = nest + newr
    #             newr = ""
    #         else:
    #             nest = nest + " " + newr
    #             newr = ""
    #     i += 1

    for i in range(0,len(s)):
        if s[i] != " ":
            newr = s[i] + newr
        elif newr != "":
            if nest == "":
                nest = nest + newr
                newr = ""
            else:
                nest = nest + " " + newr
                newr = ""
    return nest

s = str(input("Enter a string :"))
res = rev_world(s)
print("The sentence after rev :",res)