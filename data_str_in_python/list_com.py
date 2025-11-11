a = [10,20,30,[40]]
print(a)
a1 = a
a[0] = 100
a[3][0] = 400
print(a)
print(a1)
b = a.copy()
a[0] = 1000
a[3][0] = 4000
print(a)
print(a1)
print(b)