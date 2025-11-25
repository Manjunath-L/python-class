def merge_desc_to_desc_append(l1, l2):
    res = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] >= l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1

    while i < len(l1):
        res.append(l1[i])
        i += 1

    while j < len(l2):
        res.append(l2[j])
        j += 1

    return res

l1 = [100, 99, 88, 77, 55, 44, 22, 11]
l2 = [89, 76, 54, 32, 10, 1]
print(merge_desc_to_desc_append(l1, l2))
