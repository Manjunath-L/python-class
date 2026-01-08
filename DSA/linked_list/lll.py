# class Node:
#     def __init__(self,data =0,next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def createNode(self,data):
#         self.head = Node(data)
#         return self.head
    

# ref = LinkedList()
# ll = ref.createNode(100)
# print("Data :",ll.data," add:",ll.next)

class Node:
    def __init__(self,data =0,next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        
    def createArray(self):
        arr = []
        while True:
            try:
                arr.append(int(input("Enter array :")))
            except Exception as e:
                return arr
            
    def convertArrToLL(self,arr):
        self.head = Node(arr[0])
        currnewnode = self.head
        
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            currnewnode.next = temp
            currnewnode = temp
        return self.head
    
    def llTravrsal(self,head):
        newnode = head
        while newnode:
            print(newnode.data,end=" --> ")
            newnode = newnode.next
    

ref = LinkedList()
arr = ref.createArray()
print("Original Array :",arr)
head_ll = ref.convertArrToLL(arr)
print("Linked list traversal")
ref.llTravrsal(head_ll)