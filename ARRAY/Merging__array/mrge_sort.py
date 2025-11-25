def createintarr():
    l1 = []
    while True:
        try:
            n =int(input("Enter a num :"))
            l1.append(n)
        except Exception as e:
            return l1
def mergesortmerge(arr,start,mid,end):
    res = []
    i , j = start,(mid + 1)
    for k in range(0,(mid + end) + 1):
        if i <= mid and j <= end:
            if arr[i] < arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
        else:
            if i <= mid:
                res.append(arr[i])
                i += 1
            elif j <= end:
                res.append(arr[j])
                j += 1


    for k in range(0,len(res)):
        arr[start] = res[k]
        start += 1

def mergesortdivide(arr,start,end):
    if start == end:
        return
    mid = (start+end) // 2
    #LHS
    mergesortdivide(arr,start,(mid))
    #Right
    mergesortdivide(arr,(mid+1),end)
    #merging
    mergesortmerge(arr,start,mid,end)


print("Enter the ele's into array :")
arr = createintarr()
print("Array before sorted :",arr)
mergesortdivide(arr,0,len(arr)-1)
print("Array after sorted :",arr)