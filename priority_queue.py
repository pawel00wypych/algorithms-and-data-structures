import tracemalloc
import time
import random

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    """
            Priority Queue implemented using a singly linked list.
            The queue is sorted in ascending order of priority (lower number = higher priority).

            Time Complexity:
                - enqueue: O(n) (worst-case)
                - extract_min: O(1)
                - peek: O(1)
                - is_empty, size: O(1)

            Memory Complexity:
                - O(n), where n is the number of elements in the queue.

            Applications:
                - Process scheduling
                - Dijkstra’s algorithm (if using a simple list-based structure)
                - Bandwidth throttling and buffering
    """

    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        if self.head is None or self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self._size += 1

    def extract_min(self):
        if self.head is None:
            raise Exception("Queue is empty")
        node = self.head
        self.head = self.head.next
        self._size -= 1
        return {"data":node.data,"priority":node.priority}

    def peek(self):
        if self.head is None:
            raise Exception("Queue is empty")
        return {"data":self.head.data,"priority":self.head.priority}

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size


def test_prio_queue():
    queue = PriorityQueue()

    queue.enqueue(10, 2)
    queue.enqueue(20,1)
    queue.enqueue(30,5)

    print("Head element:", queue.peek())
    print("Queue size:", queue.size())

    print("extract_min:", queue.extract_min())
    print("Head after extract_min:", queue.peek())
    print("Is empty?", queue.is_empty())

    queue.extract_min()
    queue.extract_min()

    print("Is empty after extract_min all?", queue.is_empty())

    priorities = []
    for x in range(3):
        priorities.append([random.randint(1, 200) for _ in range([100, 1000, 10000][x])])

    # time complexity check:
    x = 0
    for n in [100, 1000, 10000]:
        start = time.time()
        for i in range(n):
            queue.enqueue(100, priorities[x][i])
        end = time.time()
        x += 1
        print(f"Push time: {end - start} for n = {n}")

    # memory complexity check:
    for n in [100, 1000, 10000]:
        tracemalloc.start()
        queue = PriorityQueue()
        for i in range(n):
            queue.enqueue(100, random.randint(1,200))
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        tracemalloc.stop()