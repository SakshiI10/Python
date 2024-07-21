# Searching Algorithms:
# Searching algorithms are fundamental techniques used in computer science to locate a specific element within a data structure.

# 1. Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
target = 3
result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Element found at index {result}")
else:
    print("Linear Search: Element not found")


# 2. Binary Search
# Binary search is a more efficient algorithm but requires the list to be sorted. It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; otherwise, it continues in the upper half.
def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1
    
arr = [2, 3, 4, 10, 40]
target = 3
result = binary_search(sorted(arr), target, 0, len(arr) - 1)
if result != -1:
    print(f"Binary Search: Element found at index {result}")
else:
    print("Binary Search: Element not found")


# Exponential Search:
# Exponential search is particularly useful for unbounded or infinite lists. It starts by finding a range where the target element may reside and then uses binary search within that range.
def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    return binary_search(arr, target, index // 2, min(index, len(arr) - 1))

arr = [2, 3, 4, 10, 40]
target = 10
result = exponential_search(arr, target)
if result != -1:
    print(f"Exponential Search: Element found at index {result}")
else:
    print("Exponential Search: Element not found")
