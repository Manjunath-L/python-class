class CustomStack:
    def __init__(self,max_val):
        self.stack = []
        self.min_stack = []
        self.max_val = max_val

    def push(self,val):
        if self.max_val <= len(self.stack):
            raise OverflowError("Max Size Exceeded!!!!!!")

        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty!!!!!")

        val = self.stack.pop()

        if not self.min_stack or val == self.min_stack[-1]:
            self.min_stack.pop()

    def getMin(self):
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]

    def peek(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1]



ref = CustomStack(6)
ref.push(10)
ref.push(20)
ref.push(30)
ref.push(40)
ref.push(50)
print(ref.stack)
print(ref.getMin())
print(ref.peek())
ref.pop()
ref.pop()
ref.pop()
ref.pop()
ref.pop()
print(ref.stack)
print(ref.min_stack)


