def swap_case(s):
    swap_case = " "
    i = 0
    while (i <= len(s)-1):
        ext = s[i]
        ascii = ord(ext)
        if (65 <= ascii and ascii <= 90):
            res_car = ascii + 32
            res_alp = chr(res_car)
            swap_case = swap_case + res_alp
        elif (95 <= ascii and ascii <= 122):
            res_car = ascii - 32
            res_alp = chr(res_car)
            swap_case = swap_case + res_alp
        else:
            swap_case = swap_case + ext
        i = i + 1
    return swap_case


print(swap_case("""HackerRank.com presents "Pythonist 2"."""))