'''
Stack:
1. A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle

2. Implementation: 
Stacks can be implemented using List, collection.dequeue or queue.Queue. 

3. Real-world examples of stacks:
a. Task Scheduling
b. Order Processing Systems
c. BFS in Graphs

4. Operations: T
These are basic operations that manipulate the queue:
a. Enqueue: Add an item to the end of the queue.
b. Dequeue: Remove and return the item from the front of the queue.
c. Peek/Front: Return the item at the front of the queue without removing it.
d. is_empty: Check if the queue is empty.
e. size: Return the number of items in the queue.).
'''

class Queue:
    def __init__(self):
        self._items = []
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        # Add an item to the end of the queue.
        self._items.append(item)
        self.rear += 1

    def dequeue(self):
        # Remove and return the item from the front of the queue.
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self.front]
        self.front += 1
        return item

    def peek(self):
        # Return the item at the front of the queue without removing it.
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[self.front]

    def is_empty(self):
        # Check if the queue is empty.
        return self.front == self.rear

    def size(self):
        # Return the number of items in the queue.
        return self.rear - self.front

    def __str__(self):
        # Return a string representation of the queue.
        return str(self._items[self.front:self.rear])

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)       
print(queue.dequeue())  
print(queue)       
print(queue.peek())     
print(queue.size())     
print(queue.is_empty()) 
