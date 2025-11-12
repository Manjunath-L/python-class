# a ={10,20,30,40,50}
# print(a)
# for i in a:
#     print(i)
# for i,j in enumerate(a):
#     print(i," ",j)
# a = set()
# for i in range(5):
#     print("Enter a number :")
#     data = int(input())
#     a.add(data)
# print(a)
# a.update([60,70,80])
# print(a)
# d1 = int(input("Enter the value to discard: "))
# a.discard(d1)
# print(a)

s1 = {1,2,3,4}
s2 = {3,4,5,6}
s3 = {5,6,7,8}
s4 = {1,2,3,4}
s5 = {1,2}

se1 = s1.union(s2)
print(se1)
se2 = s1.intersection(s2)
print(se2)
se3 = s1.difference(s2)
print(se3)
se4 = s1.symmetric_difference(s2)
print(se4)

print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
print(s3.isdisjoint(s1))

print(s4.issubset(s5))
print(s4.issuperset(s5))
print(s5.issubset(s4))
print(s5.issuperset(s4))