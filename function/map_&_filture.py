l = ["Rama","Sita","Ravana","Krishna","Radha"]
f = list(filter(lambda data:data.startswith("R"),l))
m = list(map(lambda data:data.upper(),l))
print(f)
print(m)


