def createintarr():
    l1 = []
    while True:
        try:
            n =int(input("Enter a num :"))
            l1.append(n)
        except Exception as e:
            return l1
print("Enter element for arr1 ")
arr1 = createintarr()
print("Enter element for arr2 ")
arr2 = createintarr()

def altered_index_arr(arr1,arr2):
    res = []
    n1,n2 = len(arr1),len(arr2)
    i , j ,k = 0,0,0
    while k < (n1+n2):
        if i < n1 and k % 2 == 0:
            res.append(arr1[i])
            i += 1
            k += 1
        elif j < n2 and k % 2 != 0:
            res.append(arr2[j])
            j += 1
            k += 1
        else:
            if i < n1:
                res.append(arr1[i])
                k += 1
                i += 1
            elif j < n2:
                res.append(arr2[j])
                k += 1
                j += 1
    return res

res = altered_index_arr(arr1,arr2)
print(res)