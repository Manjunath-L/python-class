class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def class_methode(cls,s_info):
        name,age = s_info.split()
        return cls(name,int(age))

s1 = student.class_methode("Rama 24")
print(s1.name)
print(s1.age)