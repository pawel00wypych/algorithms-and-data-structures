import time

def linear_search(to_find, data = None):
    """
        Iterate through collection a collection one element at a time.
        runtime complexity: O(n)

        Pros:
        - Fast for searches of small to medium data sets
        - Does not need to be sorted
        - Useful for data structures that do not have random access (Linked List)

        Cons:
        - Slow for large data sets
    """

    if data is None:
        raise ValueError("List of elements can't be empty!\n")
    elif to_find is None:
        raise ValueError("Object to find can't be empty!\n")

    for i in range(len(data)):
        if to_find == data[i]:
            print(f"Element {to_find} has been found at index {i}\n")
            return i

    print(f"There is not value {to_find} in list!\n")
    return None

def test_linear_search():

    elements = [1,3,5,3,11,223,2323,0,23,321,11,232,33,444,112212,2323,2222,"aasa",221121,None,23123,33,12121,6,10]
    linear_search(10, elements)

    lists = [[],[],[]]
    ranges = [100000, 1000000, 10000000]

    for r in range(len(ranges)):
        for i in range(ranges[r]):
            lists[r].append(i)

    for i in range(len(lists)):
        start = time.perf_counter()
        linear_search(lists[i][-1],lists[i])
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Linear search time: {elapsed_time:.10f} for n = {len(lists[i])} elements.")

