arr1 = [10,20,30]
arr2 = [11,22,33,11,44]
print("Before :")
print("Array1: ",arr1)
print("Array2: ",arr2)
for i in range(0,len(arr2)):
    arr1.append(arr2[i])
print("After: ")
print("Array1: ",arr1)
print("Array2: ",arr2)