# t1 = (10,20,30,40,50)
# print(t1)
# print(type(t1))
#
# t2 = ("rama",22,5.8,True)
# print(t2)
# print(len(t2))
#
# t3 = (10)
# print(type(t3))
#
# t4 = (10,)
# print(type(t4))
#
# t5 = (9)
# print(t5)
# print(type(t5))

# print("==================================")
# a = (10,20,30,40,50,(10,90))
# print(id(a))
# print(a)
#
# b = a[0:2]+(25,)+a[2:]
# print(id(b))
# print(b)
#
# c = a[0:2]+a[3:]
# print(id(c))
# print(c)
#
# student_info = ("Rama",[70,86,99])
# name,ia_marks = student_info
# print(name)
# print(ia_marks)
#
# student_info[1][0] = 76

a = (10,20,30,("python","java",(99.8,99.7)),40,50)
print(a)
print(len(a))
print(a[5])
print(a[3][0])
print(a[3][2][1])
print(a[3][2])

print(id(a))
print(id(a[3]))
print(id(a[3][2]))