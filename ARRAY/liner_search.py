def create_arr():
    l1 = []
    while True:
        try:
            n = int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1

def find_arr_ele(arr,target):
    for i in range(0, len(arr)):
        if target == arr[i]:
            return True,i
    return False,-1

print("Enter the ele's to be stored into the array:")
arr = create_arr()
target = int(input("Enter the ele to be searched: "))
flage,index = find_arr_ele(arr,target)
if flage:
    print(f"{target} found at {index}")
else:
    print(f"{target} not fount in arr")