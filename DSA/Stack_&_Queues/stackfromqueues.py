from collections import deque
class StackFromQueues:
    def __init__(self):
        self.queue = deque()

    def push(self,x):
        self.queue.append(x)
        #for top appending and poping
        for i in range(0,len(self.queue)-1):
            self.queue.append(self.queue[0])
            self.queue.pop()

    def pop(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

ref = StackFromQueues()
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
