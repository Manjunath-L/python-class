def merge_custom_to_asc_append(l1_asc, l2_desc):
    l2_asc = l2_desc[::-1]

    res = []
    i = 0
    j = 0


    while i < len(l1_asc) and j < len(l2_asc):
        if l1_asc[i] <= l2_asc[j]:
            res.append(l1_asc[i])
            i += 1
        else:
            res.append(l2_asc[j])
            j += 1


    while i < len(l1_asc):
        res.append(l1_asc[i])
        i += 1

    while j < len(l2_asc):
        res.append(l2_asc[j])
        j += 1

    return res


l1 = [1, 22, 23, 45, 56, 67]
l2 = [82, 67, 53, 35, 20, 6, 4, 2, 0]
print(merge_custom_to_asc_append(l1, l2))