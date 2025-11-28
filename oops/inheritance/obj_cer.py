class p:
    def __init__(self):
        self.a = 10

class c(p):
    def __init__(self):
        self.b = 20

c =c()
print(c.b)
print(c.a)