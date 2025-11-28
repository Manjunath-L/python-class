class A:
    def __init__(self):
        self.a = 100

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 200

class C(B):
    def __init__(self):
        super().__init__()
        self.c = 300

c1 = C()
print(c1.a)
print(c1.b)
print(c1.c)