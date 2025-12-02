a = {10, 20, 30, 10, 20, 30, 10, 20, 30}
print(a)
print(len(a))
print(hash(10))


b = {"Rama","krishna","Rama"}
print(b)
print(len(b))
print(hash("Rama"))

c = {10.1,20.2,30.3}
print(c)
print(hash(20.2))

d = {True,False,False,True}
print(d)
print(hash(True))

# se1 = frozenset([10,20,30,40])
# print(se1)
# se1.add(10)
# se1.remove(10)