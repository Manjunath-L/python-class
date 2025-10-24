arr = [1, 2, 1, 2, 3, 3, 16, 17, 18, 78]

arr_sorted = sorted(arr)
for i in range(len(arr_sorted) - 2, -1, -1):
    if arr_sorted[i] < arr_sorted[-1]:
        print(arr_sorted[i])
        break
    else:
        print("-1")

