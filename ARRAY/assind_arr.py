def create_arr():
    l1 = []
    while True:
        try:
            n = int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1

def mergeascarr(arr1,arr2):
    res = []
    i , j = 0,0
    n1,n2 = len(arr1),len(arr2)
    for k in range(0,(n1+n2)):
        if i < n1 and j <n2:
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
                k += 1
            else:
                res.append(arr2[j])
                j += 1
                k += 1
        else:
            if i<n1:
                res.append(arr1[i])
                i+= 1
                k += 1
            elif j < n2:
                res.append(arr2[j])
                j+=1
                k += 1
    return res
