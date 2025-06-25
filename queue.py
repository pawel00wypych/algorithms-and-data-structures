import tracemalloc
import time

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    """
        FIFO data structure. This queue is implemented using a singly linked list.
        All operations are O(1) time complexity because they don’t depend on the number of elements
        Memory complexity O(n), where n is the number of elements in the queue.
        Applications of Queue:
            - Operating Systems: Process scheduling, IO buffering.
            - Networking: Packet queues in routers.
            - Breadth-First Search (BFS): Traversing graphs or trees.
            - Simulation: Queuing systems like call centers or toll booths.
    """

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        head_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return head_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data

    def is_empty(self):
        return True if self.head is None else False

    def size(self):
        return self._size

def test_queue():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Head element:", queue.peek())
    print("Queue size:", queue.size())

    print("dequeue:", queue.dequeue())
    print("Head after dequeue:", queue.peek())
    print("Is empty?", queue.is_empty())

    queue.dequeue()
    queue.dequeue()

    print("Is empty after dequeue all?", queue.is_empty())

    # time complexity check:
    for n in [1000, 10000, 100000, 1000000, 10000000]:
        start = time.time()
        for i in range(n):
            queue.enqueue(100)
        end = time.time()
        print(f"Push time: {end - start} for n = {n}")

    # memory complexity check:
    for n in [1000, 10000, 100000, 1000000]:
        tracemalloc.start()
        queue = Queue()
        for i in range(n):
            queue.enqueue(i)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        tracemalloc.stop()