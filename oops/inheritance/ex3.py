class p:
    def __init__(self,a):
        self.a = a

class c(p):
    def __init__(self,a,b):
        p.__init__(self,a)
        self.b = b

c =c(10,20)
print(c.a)
print(c.b)