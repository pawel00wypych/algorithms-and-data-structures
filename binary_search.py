import time
from math import floor


def binary_search(elements, target):
    """
        Algorithm that finds the position of a target value within a sorted array.
        Half of the array is eliminated during each "step". Array have to be sorted.
        time complexity: O(log(n)) - because we disregard half of the elements
        with each iteration.
    """
    if not elements:
        raise ValueError("You must provide an array of elements!")
    elif target is None:
        raise ValueError("You must provide a target value!")

    left = 0
    right = len(elements) - 1

    while left <= right:
        middle = left + floor((right - left) / 2)
        if elements[middle] < target:
            left = middle + 1
        elif elements[middle] > target:
            right = middle - 1
        else:
            return middle

    print(f"Target value: {target} was not found in the array.")
    return -1


def test_binary_search():

    my_list = []
    for i in range(0,10000):
        my_list.append(i)

    target = 255
    print(f"Index of target value: {target} is {binary_search(my_list,target)}\n")

    target = 20000000
    print(f"Index of target value: {target} is {binary_search(my_list, target)}\n")

    lists = [[], [], []]
    ranges = [100000, 1000000, 10000000]

    for r in range(len(ranges)):
        for i in range(ranges[r]):
            lists[r].append(i)

    for i in range(len(lists)):
        start = time.perf_counter()
        binary_search(lists[i], 124)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Binary search time: {elapsed_time:.10f} for n = {len(lists[i])} elements.")