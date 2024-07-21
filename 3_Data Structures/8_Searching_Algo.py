'''Searching Algorithms:
Searching algorithms are fundamental techniques used in computer science to locate a specific element within a data structure.'''

'''1. Linear Search
a. Linear search is the simplest searching algorithm. It sequentially checks each element of the list until it finds the target value.
b. Time Complexity: O(n)
Best Case: O(1)
Worst Case: O(n)
Average Case: O(n)'''

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


''' 2. Binary Search
a. Binary search is a more efficient algorithm but requires the list to be sorted. It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, the search continues in the lower half; otherwise, it continues in the upper half.
b. Time Complexity: O(log n)
Best Case: O(1)
Worst Case: O(log n)
Average Case: O(log n)'''

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


'''3. Exponential Search:
a. Exponential search is particularly useful for unbounded or infinite lists. It starts by finding a range where the target element may reside and then uses binary search within that range.
b. Time Complexity: O(log n)
Best Case: O(1)
Worst Case: O(log i) + O(log n)
Average Case: O(log n)'''

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
