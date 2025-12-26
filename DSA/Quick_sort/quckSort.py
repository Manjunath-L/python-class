def createintarr():
    l1 = []
    while True:
        try:
            n =int(input("Enter a num :"))
            l1.append(n)
        except Exception as e:
            return l1
#
# def quickSort(arr,left,right):
#     if left >= right:
#         return
#
#     start,end = left,right
#     mid = (start + end) // 2
#     pivot = arr[mid]
#     while start <= end:
#         while arr[start] < pivot:
#             start += 1
#         while arr[end] > pivot:
#             end -= 1
#
#     if start <= end:
#         arr[start],arr[end] = arr[end],arr[start]
#         start += 1
#         end -= 1
#
#     #LHS Piovt
#     quickSort(arr,left,end)
#     #RHS Pivot
#     quickSort(arr,start,right)
#
#
# print("Enter element for arr1 ")
# arr = createintarr()
# print("Original Array :",arr)
# quickSort(arr,0,len(arr)-1)
# print("After quick sort array :",arr)

def quicksort(arr, left, right):
    if left >= right:
        return
    start, end = left, right
    mid = (start + end) // 2
    pivot = arr[mid]
    while start <= end:
        while arr[start] < pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    # LHS of pivot
    quicksort(arr, left, end)
    # RHS of pivot
    quicksort(arr, start, right)
print("Enter elements into the array: ")
arr = createintarr()
print("Original array: ", arr)
quicksort(arr, 0, len(arr)-1,)
print("After sort:", arr)