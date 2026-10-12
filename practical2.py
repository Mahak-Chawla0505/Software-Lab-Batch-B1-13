import time

def linear_search(sorted_list, target):
    """Return the index of target using a linear search, or -1 if absent."""
    for index, element in enumerate(sorted_list):
        if element == target:
            return index
    return -1

def binary_search(sorted_list, target):
    """Return the index of target using binary search, or -1 if absent."""
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        element = sorted_list[middle]
        if element == target:
            return middle
        if element < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

if __name__ == "__main__":
    values = list(range(1, 1000001)) # To check the performance of the algorithm, we can use a large list of values.
    target = int(input("Enter the target element: "))

    start_time = time.perf_counter()
    linear_result = linear_search(values, target)
    linear_time = time.perf_counter() - start_time

    start_time = time.perf_counter()
    binary_result = binary_search(values, target)
    binary_time = time.perf_counter() - start_time

    print(f"Linear search: index {linear_result}, time {linear_time:.8f} seconds")
    print(f"Binary search: index {binary_result}, time {binary_time:.8f} seconds")