arr = [1,2,3]
print("Type of DS: ",type(arr))
print("Ele's in DS: ",arr)
print("Count of num of ele in DS: ",len(arr))
print("=====================================")
t = (1,2,3,4,4,3)
print("Type of DS: ",type(t))
print("Ele's in DS: ",t)
print("Count of num of ele in DS: ",len(t))
print("=====================================")
s = 'qweettyyy'
print("Type of DS: ",type(s))
print("Ele's in DS: ",s)
print("Count of num of ele in DS: ",len(s))
print("=====================================")
dict = {101:"abc",102:"bbc"}
print("Type of DS: ",type(dict))
print("Ele's in DS: ",dict)
print("Count of num of ele in DS: ",len(dict))
print("=====================================")
s1 = {1,2,3,3,4,5,6,5,4}
print("Type of DS: ",type(s1))
print("Ele's in DS: ",s1)
print("Count of num of ele in DS: ",len(s1))
print("=====================================")

arr = [ ]
print(len(arr))
# arr[0] = 55
arr.append(10)
arr.append("abc")
arr.append(23.7)
print(arr)
print(len(arr))
arr.insert(1,25)
arr.insert(100,101)
print(arr)
arr[4] = 200
print(arr)
# arr[10] = 333
arr.extend([10,20])