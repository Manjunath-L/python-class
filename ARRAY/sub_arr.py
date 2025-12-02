def create_subarr(arr):
    for i in range(0,len(arr)):
        sub = []
        for j in range(i,len(arr)):
            sub.append(arr[j])
            print(sub,end= " ")
        print()

arr = [1,2,3,4,5]
create_subarr(arr)
