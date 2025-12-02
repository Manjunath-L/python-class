def create_arr():
    l1 = []
    while True:
        try:
            n = int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1


def segration(arr):
    dict = {}
    for i in range(0,len(arr)):
        if arr[i] in dict:
            dict[arr[i]] = dict[arr[i]] + 1
        else:
            dict[arr[i]] = 1

    dup = []
    nondup = []
    unique = []

    for key,val in dict.items():
        if val > 1:
            dup.append(key)
        if val >= 1:
            nondup.append(key)
        if val == 1:
            unique.append(key)

    return dup,nondup,unique


arr = create_arr()
dupres, nondupres, uniqueres = segration(arr)
print(dupres)
print(nondupres)
print(uniqueres)