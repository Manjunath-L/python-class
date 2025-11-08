# a=[10,20,30,40,50,60,70]
# for i in a:
#     print(i)
# print(a)
# a.remove(30)
# print(a)
# a.pop()
# a.pop()
# print(a)
# a.pop(1)
# print(a)
# print(a.count(50))
# print(a.index(10))
# a.clear()
# print(a)
# del a
# a = [10,20,30,40]
# print(a)
# for i in a:
#     print(i)
# for i,j in enumerate(a):
#     print(i," ",j)
# del a
# a= list(range(10))
# b= list(range(10,15))
# c= list(range(10,20,2))
# print(a)
# print(b)
# print(c)

# a = [10,20,30,40,50]
# b= []
# for data in a:
#     newdata = data + 1
#     b.append(newdata)
# print(b)
# del b
# b = [data+1 for data in a]
# print(b)

a = [1,2,3,4,5]
b = []
for data in a:
    newdata = data ** 2
    b.append(newdata)
print(b)
del b
b = [data**2 for data in a]
print(b)