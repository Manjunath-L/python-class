def swapping(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def recc_permutation(i,arr,res):
    if i == len(arr):
        res.append(arr[:])
        return

    for j in range(i,len(arr)):
        swapping(arr,i,j)
        recc_permutation((i+1),arr,res)
        swapping(arr,j,i)

def permutation(arr):
    res = []
    recc_permutation(0,arr,res)
    return res

arr = [4,5,6]
res = permutation(arr)
print(res)