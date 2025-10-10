# class Hero:
#     def __init__(self):
#         self.name = "sudeep"
#         self.age = 52
#         self.mob = 99887
#         self.add = "JPnagur"

#     def sing(self):
#         print("hero is singing")
#     def act(self):
#         print("hero is acting")
#     def dance(self):
#         print("hero is dancing")

# h1 = Hero()
# print(h1.name)
# print(h1.age)
# print(h1.mob)
# print(h1.add)

# #modifing
# h1.name = "sudeepa"
# h1.mob = 987654

# #adding
# h1.height = 6.1
# h1.noOfMovice = 40

# h2 = h1
# h3 = h2

# print(h3.name)
# print(h2.age)
# print(h1.mob)
# print(h3.add)
# print(h2.height)
# print(h3.noOfMovice)

# h1.sing()
# h2.act()
# h3.dance()

# for i in range(10):
#     print(i)

#
# a = int(input("Enter a number: "))
# print(a)
# print(type(a))
# 
# print(10+3+4+9.000) # addition
# print(10+30+90) # addition
# print(20+40) # addition
# print(+78) #represents +Ve num
# print(+78.99) #represents +Ve num
# print(50.6788438349+83498023) # addition
# print("===========================")
# print(1-1-2-4-5-6)
# print(2-2-5-6)
# print(3-3-5-6-7)
# print("=====================")
# print(68*78)
# print(68*8)
# print(6*78)
# # print(*78)
# print("======================")
# print(2**4)
# print(4**2)
# print(4**5)
# print(5**4)

#
# print(10//2)
# print(22//7)
# print("===============================")
# print(10/2)
# print(22/7)
# print("==========================")
# print(10%2)
# print(22%7)
# print(999%8383)
# print(45%45)
#
# print(100 > 9)
# print(1*10 >= 10)
# print(30*6 <= 36*1)
# print(True != False)
# print(10 <= (100 -90))
# print(2 >= (100 ** 0))
# print(False ** True)

# print(True and True and True)
# print(False and (True ** 2))
# print(-99 and 90 or 90)
# print(50 or "domf" and 60 )
# print(90 and ())
# print(2 >= (100 ** 0))
# print(False ** True)



# a = 10
# print(a)
# b=(2*5)
# print(b)
# c=(10**1)
# print(c)
# print(a==b==c)
# print(id(a)==id(b)==id(c))
# c=15
# print(c)
# print(id(c))
# c=20
# print(c)
# print(id(c))
# c=25
# print(c)
# print(id(c))
# d=1,2,3
# print(d)
# print(type(d))
# print(id(d))
#
# a = 5
# print(a)
# print(type(a))
# b=5.5
# print(b)
# print(type(b))
# c="rama"
# print(c)
# print(type(c))
#
#
# a= 5
# print(a)
# print(id(a))
# b=a
# print(b)
# print(id(b))
# print(a is b)
# c=a
# print(c)
# print(id(c))
# print(a is c)
#
# a=10
# b=10
# c=10
# print(a)
# print(b)
# print(c)
# print(id(a))
# print(id(b))
# print(id(c))
# print( a is  b)
# print(  b is  c)
# print( c is a )
#
# d=-10
# e=-9
# f=-7
# print(d)
# print(e)
# print(f)
# print(id(a))
# print(id(b))
# print(id(c))
# print(d is e)
# print( a is d )
# print( d is b )
#
# a=287
# b=287
# print(id(a))
# print(id(b))
# print(a is b)


#
# l1 = [1,3,8,-9]
# print(l1[1])
# print(l1[3])
# print(3 in l1)
# print([-9] in l1)
# a=(2*4)
# print(a not in l1)
# print(8 in a)
#
# print("8" in "88")

# a = 5
# b = (4+1)
# c = (5-0)
# print(a is 5)
# print(a is not "b")
# print("===================")
# print(a is b)
# print(b is not c)
# print(a is id(5))
#
# class cal:
#     def __init__(self):
#         self.a = 100
#         self.b = 200
#
#     def add(self):
#         x = 10
#         y = 20
#         z = x + y
#         return  z
#
# c1 = cal()
# print(c1.a)
# print(c1.b)
# res1 = c1.add()
# print(res1)
#
#
# n1 = int(input("Enter num 1 : "))
# n2 = int(input("Enter num 2 : "))
# n3 = int(input("Enter num 3 : "))
#
# if n2 < n1 > n3:
#     print(n1)
# elif n1 < n2 > n3:
#     print(n2)
# else:
#     print(n3)
# print("Calcutied..........")

#
# n1 = int(input("Enter a number : "))
# #
# # if n1 <= 0:
# #     print("Neutral")
# # elif n1 % 3 == 0 and n1 % 5 == 0:
# #     print("Fizz Buzz Num")
# # elif n1 % 5 == 0:
# #     print("Buzz Num")
# # elif n1 % 3 == 0:
# #     print("Fizz Num")
# # else:
# #     print("You have entered a number")
#
# if n1 > 0:
#     if n1 % 3 == 0 and n1 % 5 == 0:
#         print("Fizz Buzz")
#     elif n1 % 3 == 0:
#         print("Fizz")
#     elif n1 % 5 == 0:
#         print("Buzz")
#     else:
#         print("You have entered a number")
# else:
#     print("Neutral")
#
# class cal:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#     def add(self,x,y):
#         z = x+y
#         return  z
#
# c1 = cal()
# print(c1.a)
# print(c1.b)
# res1 = c1.add(111,222)
# print(res1)
#
# class cla:
#     def __init__(self):
#         self.x = 10
#         self.y = 20
#     def add(self):
#         self.x=10
#         self.=30
#         c=a+b
#         print("the sum is",c)
#     def diff(self):
#         n1 = 50
#         n2 = 40
#         n3 = n1 - n2
#         print("The diff is" , n3)
#
# c1 = cla()
# c1.add()
# c1.diff()
#
# class student:
#     def __init__(self):
#         self.name = "Rama"
#         self.age = 22
#         self.height = 5.6
#
#     def display(self):
#         print(self.name )
#         print(self.height )
#         print(self.age )
#
# s1 = student()
# s1.display()
# print(s1.name)
# print(s1.age)
# print(s1.height)

# var = range(7)
# print(range(1,5))
# print(range(10,15,2))
# print(range(7))
# print(range())
# n = int(input("Enter a num :"))
# for i in range(n,(1-1),-2):
#     print(i,end=" ")
# print("\nProg exec")
# print("last updated value :",i)
#
# class Heroine:
#     def __init__(self):
#         self.name = "Ramya"
#         self.age = 32
#         self.mod = 1234
#
#     def act(self):
#         self.heigh = 5.6
#         self.color = "White"
#
# h1 = Heroine()
# print(h1.name)
# print(h1.age)
# print(h1.mod)
# h1.act()
# h1.name = "Radhika"
# h1.addr = "Bang"
# print(h1.name)
# print(h1.age)
# print(h1.mod)
# print(h1.addr)
#
# class Student:
#     def __init__(self,name,age,height,addr):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.addr = addr
#
# s1=Student("rama",23,5.8,"Beng")
# s2=Student("sita",22,5.6,"chin")
#
# print(s1.name,s1.age)
# print(s2.name,s2.age)
#
# class Demo:
#     x = 99
#     y = 88
#     def __init__(self):
#         self.a=10
#         self.b = 20
#
# d1=Demo()
# d2=Demo()
# d3=Demo()
# print(Demo.x)
# print(Demo.y)
# Demo.x = 889
# Demo.y = 888
# print(Demo.x)
# print(Demo.y)

#
# l1=[1,2,3]
# for i in range(0,3):
#     print("Index :", i," Ele:",l1[i])


# n = int(input("Enetr a number :"))
# i=3
# while i <= n:
#     print(i,end=" ")
#     i = i+1
# print("\n pro excuted")
# print("last i:" , i)


#
# class Farmer:
#     r = 2.5
#     def __init__(self,p,t):
#         self.p = p
#         self.t = t
#
#     def calcu(self):
#         si = (self.p * self.t *(Farmer.r))/100
#         print(si)
#
#
# f1 = Farmer(100000,2)
# f2 = Farmer(1500000,4)
# f3 = Farmer(3000000,7)
# f1.calcu()
# f2.calcu()
# f3.calcu()

# str1 = "Rama"
# print(str1)
# print(len(str1))
# print(type(str1))

n = int(input("Enter a number :"))
i = 1
while n > 0:
    print(n)
    n = n - i
    i += 1