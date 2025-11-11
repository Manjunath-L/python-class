a = range(5,20)
b = [ ]
for data in a:
    if data % 2 == 0:
        b.append(data)
print(b)

b1 = [data for data in range(5,20) if data % 2 == 0]
print(b1)

b2 = []
for data in a:
    if data % 2 != 0:
        b2.append(data)
print(b2)

b3 = [data for data in range(5,20) if data % 2 != 0]
print(b3)