def merge_desc_to_asc_append(l1, l2):
    l1_asc = l1[::-1]
    l2_asc = l2[::-1]

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

l1 = [100, 99, 88, 77, 55, 44, 22, 11]
l2 = [89, 76, 54, 32, 10, 1]
print(merge_desc_to_asc_append(l1, l2))