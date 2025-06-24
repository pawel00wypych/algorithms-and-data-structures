import time
import tracemalloc

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """
        This stack is implemented using a singly linked list.
        All operations are O(1) time complexity because they don’t depend on the number of elements in the stack.
        Total Memory Complexity: O(n), where n is the number of elements in the stack.
    """

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow - Stack is empty!")
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def size(self):
        return self._size




def test_stack():
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped:", stack.pop())
    print("Top after pop:", stack.peek())
    print("Is empty?", stack.is_empty())

    stack.pop()
    stack.pop()

    print("Is empty after popping all?", stack.is_empty())

    # time complexity check:
    for n in [1000, 10000, 100000, 1000000, 10000000]:
        start = time.time()
        for i in range(n):
            stack.push(100)
        end = time.time()
        print(f"Push time: {end - start} for n = {n}")

    # memory complexity check:
    for n in [1000, 10000, 100000, 1000000]:
        tracemalloc.start()
        stack = Stack()
        for i in range(n):
            stack.push(i)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        tracemalloc.stop()