l =[]
i=0
while i<=4:
    data = int(input("Enter the value :"))
    l.insert(i,data)
    i+=1
print(l)
k = list(map(lambda n: n+30,l))
print(k)