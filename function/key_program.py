l = [ ]
i = 0
while i <= 4:
    print("Enter the value :")
    da =int(input())
    l.insert(i,da)
    i += 1

print(l)
for i in l:
    print(i)

i = 0
n = len(l)
while i <= n:
    print(l[i])
    i= i + 1