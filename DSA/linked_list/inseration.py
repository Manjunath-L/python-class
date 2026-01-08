class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def createArray(self):
        arr = []
        print("Enter element for array :")
        while True:
            try:
                arr.append(int(input("Enter array :")))
            except Exception as e:
                return arr

    def convertArrToLL(self, arr):
        self.head = Node(arr[0])
        currnewnode = self.head

        for i in range(1, len(arr)):
            temp = Node(arr[i])
            currnewnode.next = temp
            currnewnode = temp
        return self.head

    def llTravrsal(self, head):
        newnode = head
        while newnode:
            print(newnode.data, end=" --> ")
            newnode = newnode.next

    def lllLength(self,head):
        mover = head
        count = 0
        while mover:
            count += 1
            mover = mover.next
        return count

    def deleteLLHead(self,head):
        mover = head
        head = mover.next
        return head

    def deleteLLTail(self,head):
        mover = head
        while mover:
            if mover.next.next == None:
                mover.next = None
                break
            else:
                mover = mover.next
        return
    # Insertion at Head
    def insertAtHeadLL(self, head, data):
        newnode = Node(data)
        newnode.next = head
        head = newnode
        return head

# Insertion at Tail
    def insertAtTailLL(self, head, data):
        newnode = Node(data)
        if not head:
            return newnode
        currnode = head
        while currnode.next:
            currnode = currnode.next
        currnode.next = newnode
        return head



ref = LinkedList()
arr = ref.createArray()
print("Original Array :", arr)
head_ll = ref.convertArrToLL(arr)
print("Linked list traversal")
ref.llTravrsal(head_ll)
len1 = ref.lllLength(head_ll)
print("\n-----------------------------------------")
print("The length of linked list :",len1)
print("\n-----------------------------------------")
print("After deleting llHead")
head = ref.deleteLLHead(head_ll)
ref.llTravrsal(head)
print("\n-----------------------------------------")
print("After deleting tail ")
ref.deleteLLTail(head)
ref.llTravrsal(head)
print("\n=======================================")
data = int(input("Enter value to insert at head: "))    
print(f"After inserting {data} at head of Linked List:")
head = ref.insertAtHeadLL(head, data)
ref.llTravrsal(head)
print("\n=======================================")
data = int(input("Enter value to insert at tail: "))    
print(f"After inserting {data} at tail of Linked List:")
head = ref.insertAtTailLL(head, data)
ref.llTravrsal(head)
