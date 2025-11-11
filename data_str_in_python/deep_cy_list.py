import copy

a = [10,20,30,[40]]
print(a)
a1 = a
b = copy.deepcopy(a)
a[0] = 100
a[3][0] = 400
print(a)
print(a1)
print(b)
