class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        # Create a dummy head node with value None
        self.head = ListNode()
        self.size=0

    def insertAtHead(self, data):
        # Insert a new node at the head of the list
        new_node = ListNode(data)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size+=1

    def insertAtTail(self, data):
        # Insert a new node at the tail of the list
        new_node = ListNode(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.size+=1

    def deleteAtHead(self):
        # Delete the node at the head of the list
        if self.head.next is not None:
            self.head.next = self.head.next.next

    def printLinkedList(self):
        # Print the linked list starting from the first actual node
        current = self.head.next
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print(None)

    def reverse(self):
        i=self.head.next
        results=[]
        while i!=None:
            results.append(i.value)
            i=i.next
        print(results)
        print("the value of results is",list(reversed(results)))

    def reverseList(self, head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            self.head = prev

    def hasCycle(self, head):
        i = self.head
        print(i.value)
        result=[]
        while i.next!=None:
            result.append(i.value)
            print(f"result list is {result}")
            i = i.next
            print(i.value)
        print(result)
        if i.next in result:
            print("HELLO")
            print(True)
        else:
            print("HII")
            print(False)






# Example usage:
# Create an empty singly linked list
sll = SinglyLinkedList()

# Insert nodes at the head and tail of the list
sll.insertAtHead(1)
sll.insertAtTail(2)
sll.insertAtTail(3)
sll.insertAtTail(4)
sll.insertAtTail(5)
sll.insertAtTail(6)
sll.insertAtTail(7)




# Print the linked list
print("Linked List:")
sll.printLinkedList()
'''
# Delete the head node and print the updated list
sll.deleteAtHead()
print("Linked List after Deleting Head:")
sll.printLinkedList()
sll.insertAtHead(1)
sll.printLinkedList()
'''


sll.hasCycle(sll)
