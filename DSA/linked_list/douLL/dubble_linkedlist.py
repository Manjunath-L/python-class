class Node:
    def __init__(self, data=0, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def create_array(self):
        array = []
        print("Enter elements for array (non-number to stop):")
        while True:
            try:
                array.append(int(input("Enter element: ")))
            except:
                return array

    def array_to_dll(self, array):
        if not array:
            return None

        head = Node(array[0])
        previous = head

        for i in range(1, len(array)):
            current = Node(array[i], previous)
            previous.next = current
            previous = current

        return head

    def traverse(self, head):
        if head is None:
            return

        current = head
        while current:
            print(f"<-- {current.data} -->", end=" ")
            current = current.next

    # delete head node
    def delete_head(self, head):
        if head is None or head.next is None:
            return None

        new_head = head.next
        head.next = None
        new_head.prev = None
        return new_head

    # delete tail node
    def delete_tail(self, head):
        if head is None or head.next is None:
            return None

        current = head
        while current.next:
            current = current.next

        previous = current.prev
        previous.next = None
        current.prev = None
        return head

    # insert at head
    def insert_head(self, head, data):
        new_node = Node(data)
        new_node.next = head
        if head:
            head.prev = new_node
        return new_node

    # reverse using stack
    def reverse_dll(self, head):
        if head is None:
            return None
        stack = []
        current = head
        while current:
            stack.append(current.data)
            current = current.next
        current = head
        while current:
            current.data = stack.pop()
            current = current.next
        return head

    def length(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count

    # delete at specific position
    def delete_at_position(self, head, position):
        total_nodes = self.length(head)

        if position > total_nodes or position < 1:
            print("Invalid position")
            return head

        if position == 1:
            return self.delete_head(head)

        if position == total_nodes:
            return self.delete_tail(head)

        count = 1
        previous = head
        current = head.next

        while current:
            count += 1
            if count == position:
                previous.next = current.next
                current.next.prev = previous
                current.next = None
                current.prev = None
                break
            previous = current
            current = current.next

        return head

    # delete by value
    def delete_by_value(self, head, value):
        if head is None:
            print("List is empty")
            return None

        current = head

        # case 1: deleting head
        if current.data == value:
            return self.delete_head(head)

        while current:
            if current.data == value:
                # case 2: deleting tail
                if current.next is None:
                    return self.delete_tail(head)

                # case 3: deleting middle node
                current.prev.next = current.next
                current.next.prev = current.prev

                current.next = None
                current.prev = None
                return head

            current = current.next

        print("Value not found")
        return head

    def insert_tail(self, head, data):
        new_node = Node(data)

        # case 1: empty list
        if head is None:
            return new_node

        current = head

        # move to last node
        while current.next:
            current = current.next

        # link new node
        current.next = new_node
        new_node.prev = current

        return head


dll = DoublyLinkedList()

array = dll.create_array()
head = dll.array_to_dll(array)

print("\nOriginal List:")
dll.traverse(head)

print("\n\nAfter deleting head node:")
head = dll.delete_head(head)
dll.traverse(head)

print("\n\nAfter deleting tail node:")
head = dll.delete_tail(head)
dll.traverse(head)

print("\n\nAfter inserting at head:")
data = int(input("Enter head data: "))
head = dll.insert_head(head, data)
dll.traverse(head)

print("\n\nAfter deleting at specific position:")
pos = int(input("Enter position: "))
head = dll.delete_at_position(head, pos)
dll.traverse(head)

print("\nAfter deleting value:")
val = int(input("Enter value to delete: "))
head = dll.delete_by_value(head, val)
dll.traverse(head)



print("\nAfter inserting at tail:")
val = int(input("Enter value to delete: "))
head = dll.insert_tail(head, val)
dll.traverse(head)