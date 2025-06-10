'''
Sorting Algorithm:
1. Sorting techniques are used to arrange data(mostly numerical) in an ascending or descending order.

2. Real World Application:
a. Dictionary
b. Contact list

3. Types of Order:
a. Increasing Order, For example: 1, 2, 3, 4, 5
b. Decreasing Order, For Example: 5, 4, 3, 2, 1
c. Non-Increasing Order, For Example: 5, 4, 3, 2, 2, 1
d. Non-Decreasing Order, For Example: 1, 2, 2, 3, 4, 5
'''

'''1. Bubble Sort
a.  Bubble Sort is a simple sorting algorithm. This sorting algorithm repeatedly compares two adjacent elements and swaps them if they are in the wrong order.
b. Time Complexity: O(n^2)'''

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 1, 4, 2, 8]
bubbleSort(arr)
print("Sorted array using Bubble Sort:", arr)


'''
2. Selection Sort
a. This sorting technique repeatedly finds the minimum element and sort it in order. 
b. During the execution of Selection Sort for every iteration, the minimum element of the unsorted subarray is arranged in the sorted subarray. 
c. Selection Sort is a more efficient algorithm than bubble sort. 
d. Time-Complexity: O(n^2)'''

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum element is the first element
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [5, 1, 4, 2, 8]
selectionSort(arr)
print("Sorted array using Selection Sort:", arr)


'''3. Insertion sort
a. This sorting algorithm maintains a sub-array that is always sorted. 
b. Values from the unsorted part of the array are placed at the correct position in the sorted part. 
c. Time-Complexity:
i. Average and Worst case: O(n^2) 
ii. Best case: O(n)'''

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [5, 1, 4, 2, 8]
insertionSort(arr)
print("Sorted array using Insertion Sort:", arr)
