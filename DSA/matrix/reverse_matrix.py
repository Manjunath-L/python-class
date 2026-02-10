def create_matrix():
    outer = []
    n = int(input("Enter row size :"))
    m = int(input("Enter col size :"))
    for i in range(0,n):
        inner = []
        for j in range(0,n):
            inner.append(int(input("Enter val :")))
        outer.append(inner)
        print()
    return outer

def reverse_matrix(arr):
    n = len(arr)
    for i in range(0,n):
        inner_array = arr[i]
        right ,left = len(inner_array)-1 , 0
        while left < right:
            inner_array[left],inner_array[right] = inner_array[right] , inner_array[left]
            right = right - 1
            left = left + 1

arr = create_matrix()
print(arr)
reverse_matrix(arr)
print(arr)
