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

    #deleting head node in dbll
    def deleteHead(self,head):
        if head == None or head.next == None:
            return None
        prv = head
        newHead = prv.next
        prv.next = None
        return newHead

    def deleteTail(self,head):
        mover = head
        if mover == None or mover.next == None:
            return None

        while mover.next != None:
            mover = mover.next

        prev = mover.prv
        prev.next = None
        mover.prv = None
        return head

    #insert head
    def insertHead(self,head,data):
        mover = Node(data)
        mover.prv = None
        mover.next = head
        head = mover
        return head
    #insert tail
    #reverse stack
    def reversedbll(self,head):
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
    #delete from specfic loc in dblll
    def lengthDbll(self,head):
        count = 0
        mover = head
        while mover:
            count += 1
            mover = mover.next
        return count

    def deleteSpecfic(self,head,pos):
        n = self.lengthDbll(head)
        if pos > n:
            print("Invalid position")
            return None
        elif pos == 1:
            newHead = self.deleteHead(head)
            return newHead
        elif pos == n:
            newHead = self.deleteTail(head)
            return  newHead
        else:
            count = 1
            prev = head
            mover = prev.next
        while mover:
            count += 1
            if count == pos:
                prev.next = mover.next
                mover.next.prv = mover.prv
                mover.next = None
                mover.prv = None
                break
            else:
                prev = mover
                mover = mover.next
        return head


ref = DBll()
arr = ref.createArray()
head = ref.convertArrDbll(arr)
ref.traversal(head)
print("\n***********************")
print("After deleting head node")
head = ref.deleteHead(head)
ref.traversal(head)
print("\n%%%%%%%%%%%%%%%%%%%%%%%")
print("After deleting tail node")
head = ref.deleteTail(head)
ref.traversal(head)
print("\n%%%%%%%%%%%%%%%%%%%%%%%")
print("After inserting head node")
data = int(input("Enter head data = "))
head = ref.insertHead(head , data)
ref.traversal(head)
print("\n%%%%%%%%%%%%%%%%%%%%%%%")
print("After Deleting at spefic pos node")
pos = int(input("Enter the positon = "))
head = ref.deleteSpecfic(head , pos)
ref.traversal(head)

