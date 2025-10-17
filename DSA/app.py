arr = [1, 2, 1, 2, 3, 3, 16, 17, 18, 78]

arr_sorted = sorted(arr)
for i in range(len(arr_sorted) - 2, -1, -1):  # loop backward
    if arr_sorted[i] < arr_sorted[-1]:  # find next smaller than max
        print(arr_sorted[i])
        break
    else:
        print("-1")
