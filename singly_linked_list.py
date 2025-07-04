
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
        A singly linked list (SLL) is a fundamental data structure used in computer science to store a sequence of elements in linear order.
        Each element in the list is called a node, and each node contains data and pointer to next node. SLL is efficient for
        insertions and deletions but not for searching. Can only be traversed in one direction.
        Used in:
            - Implementing stacks and queues
            - Memory-efficient dynamic data structures
            - Applications in graph algorithms, symbolic computations, and more
        Time complexity:
            Insert (begin)	O(1)
            Insert (end)	O(n)
            Delete (begin)	O(1)
            Delete (end)	O(n)
            Search	        O(n)
            Access	        O(n)
        Memory complexity O(n), where n is the number of elements in the SLL.
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):

        if self.head is None:
            raise IndexError("Linked list is empty")


        current = self.head
        if current.data == data:
            self.head = current.next
            current.next = None # Clears the next reference of the deleted node to help Python's garbage collector.
            return
        else:
            while current.next:
                    if current.next.data == data:
                        next_node = current.next
                        current.next = current.next.next
                        next_node.next = None
                        return

                    current = current.next

        raise ValueError(f"Value {data} not found in the list")

    def find(self, data):
        if self.head is None:
            raise IndexError("Linked list is empty")
        else:
            current = self.head
            while current:
                if current.data == data:
                    return True
                else:
                    current = current.next
            return False

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")