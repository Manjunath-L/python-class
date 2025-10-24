# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

l = [ ]
i = 0
n = int(input("Enter list size :"))
while i <= n-1:
    print("Enter the value :")
    da =int(input())
    l.insert(i,da)
    i += 1

print(l)

k = list(filter(lambda num:(num % 2 == 0),l))
# k = list(filter(even,l))
print(k)

# i = 0
# while i <= 4:
#     ext = l[i]
#     status = even(ext)
#     if status == True:
#         print(l[i])
#     i= i + 1

