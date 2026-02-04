class QueusfromStack:
    def __init__(self):
        self.inputstack = []
        self.outputstack = []

    #inserting operation
    def push(self,x):
        self.inputstack.append(x)

    #reteiving the top element from queue(stack)
    def peek(self):
        if self.outputstack:
            return self.outputstack[-1]
        else:
            while self.inputstack:
                x1 = self.inputstack.pop()
                self.outputstack.append(x1)

            # if self.outputstack:
            #     return self.outputstack[-1]
            # else:
            #     return None

            return self.outputstack[-1] if self.outputstack else None
    #deleting the top element from queue(stack)
    def pop(self):
        if self.outputstack:
            return  self.outputstack.pop()
        else:
            while self.inputstack:
                self.outputstack.pop(self.inputstack.pop())

            return  self.outputstack.pop() if self.outputstack else None


ref = QueusfromStack()
ref.push(1)
ref.push(2)
ref.push(3)
ref.push(4)
ref.push(5)
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
print(ref.peek())
print(ref.pop())
