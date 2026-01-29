class Node:
    def __init__(self,data=0,prv=None,next=None):
        self.data = data
        self.prv = prv
        self.next = next

class DBll:
    def createArray(self):
        arr = []
        print("Enter element for array")
        while True:
            try:
                arr.append(int(input("Enter element :")))
            except Exception as e:
                return arr

    def convertArrDbll(self,arr):
        if arr == []:
            return None

        head = Node(arr[0])
        prv = head
        for i in range(1,len(arr)):
            curr = Node(arr[i],prv)
            prv.next = curr
            prv = curr

        return head

    def traversal(self,head):
        if head == None:
            return None
        mover = head
        while mover:
            # print(f" {id(mover) if mover else None}<-- {mover.data} --> {id(mover.next) if mover.next else None}",end=" ")
            print(f" <-- {mover.data} --> ",end=" ")
            mover = mover.next


    def reversedbll(self, head):
        if head == None:
            return None
        mover = head
        stack = []
        while mover:
            stack.append(mover.data)
            mover = mover.next
        mover = head
        while mover:
            mover.data = stack.pop()
            mover = mover.next
        return head

    def palindrome(self, head):
        if head == None:
            return None
        mover = head
        stack = []
        while mover:
            stack.append(mover.data)
            mover = mover.next
        mover = head
        while mover:
            if mover.data != stack.pop():
                return False
            mover = mover.next
        return True

ref = DBll()
array = ref.createArray()
head = ref.convertArrDbll(array)
ref.traversal(head)
print("\n========================")
print("Array after reversal 1 :")
head = ref.reversedbll(head)
ref.traversal(head)
print("\n========================")
flage = ref.palindrome(head)
if flage:
    print("Is palindrome")
else:
    print("is not palindrome")