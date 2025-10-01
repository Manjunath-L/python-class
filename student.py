# class student():
#     name = "Manju"
#     id = 123
#     ph_nu = 123456789
#     email = "manju@gmail.com"
#
#     def study(self):
#         print(self.name,"is Studying")
#
#     def play(self):

#         print(self.name , " is Playing")
#
#     def sleep(self):
#         print(self.name,"is sleeping")
#
#
# obj_num = int(input("Enter how may obj do you want : "))
#
# for _ in range(obj_num):
#     s1=student()
#     print("student name :",s1.name)
#     print("student phone number :",s1.ph_nu)
#     print("student email :",s1.email)
#     print("student id :",s1.id)
#     s1.study()
#     s1.play()
#     s1.sleep()
#     print('<----------------------->')

# logical entity

class cal:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        print('Sum :' , (self.n1 + self.n2))

    def sub(self):
        print('Sub :',(self.n1 - self.n2))

    def mul(self):
        print('product :',(self.n1 * self.n2))


n1 = int(input('Enter number 1 : '))
n2 = int(input('Enter number 2 : '))

cal_opr = cal(n1,n2)
print('The output of perfroming operation on',cal_opr.n1 ,'and' ,cal_opr.n2 ,'is :' )
print('Sum :' ,cal_opr.add() )
print('Difference :' , cal_opr.sub())
print('Product :' , cal_opr.mul())




