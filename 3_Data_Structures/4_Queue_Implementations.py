# Enqueue using List at end, beginning or certain position:
print("Enqueue")
class Queue:
    def __init__(self, max_size):
        self.items = []
        self.front = 0
        self.rear = 0
        self.max_size = max_size
    
    def is_full(self):
        # Check if the queue is full.
        return len(self.items) >= self.max_size
    
    def enqueue_end(self, item):
        # Add an item to the end of the queue.
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return
        self.items.append(item)
        self.rear += 1
    
    def enqueue_beginning(self, item):
        # Add an item to the beginning of the queue.
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return
        self.items.insert(0, item)
        self.rear += 1
    
    def enqueue_middle(self, item, position):
        # Add an item to a specific position in the queue.
        if self.is_full():
            print("Queue is full. Cannot enqueue item.")
            return
        if position < 0 or position > len(self.items):
            raise IndexError("Position out of bounds")
        self.items.insert(position, item)
        self.rear += 1

queue = Queue(max_size=5)

# Enqueue items at the end
queue.enqueue_end(1)
queue.enqueue_end(2)
queue.enqueue_end(3)
print("Queue after enqueuing at the end:", queue.items)

# Enqueue item at the beginning
queue.enqueue_beginning(0)
print("Queue after enqueuing at the beginning:", queue.items)

# Enqueue item in the middle
queue.enqueue_middle(1.5, 2)
print("Queue after enqueuing in the middle:", queue.items)

# Try to enqueue items beyond the max size
queue.enqueue_end(4)


# Dequeue using List at end, beginning or certain position:
print("\nDequeue")
class Queue:
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = items
        self.front = 0
        self.rear = len(self._items)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0
    
    def dequeue_end(self):
        """Remove and return the item from the end of the queue."""
        if self.is_empty():
            return "Queue is empty. Cannot dequeue item."
        self.rear -= 1
        return self._items.pop()
    
    def dequeue_beginning(self):
        """Remove and return the item from the beginning of the queue."""
        if self.is_empty():
            return "Queue is empty. Cannot dequeue item."
        self.front += 1
        return self._items.pop(0)
    
    def dequeue_middle(self, position):
        """Remove and return the item from a specific position in the queue."""
        if self.is_empty():
            return "Queue is empty. Cannot dequeue item."
        if position < 0 or position >= len(self._items):
            raise IndexError("Position out of bounds")
        self.rear -= 1
        return self._items.pop(position)

# Example usage
queue = Queue([1, 2, 3])

# Dequeue item from the end
queue.dequeue_end()
print("Queue after dequeuing from the end:", queue._items)

# Dequeue item from the beginning
queue.dequeue_beginning()
print("Queue after dequeuing from the beginning:", queue._items)

# Dequeue item from the middle
queue.dequeue_middle(0)
print("Queue after dequeuing from the middle:", queue._items)

# Attempt to dequeue from an empty queue
print("Dequeued from empty queue (end):", queue.dequeue_end())


'''
4. Time Complexities:
Insertion (at the end): O(1) on average (amortized)
Example: lst.append(item).

Insertion (at the beginning or middle): O(n)
Example: lst.insert(0, item) or lst.insert(i, item).

Deletion (from the end): O(1)
Example: lst.pop().

Deletion (from the beginning or middle): O(n)
Example: lst.pop(0) or del lst[i].

Access (by index): O(1)
Example: lst[i] where i is the index.

Search (by value): O(n)
Example: value in lst or lst.index(value).

Slicing: O(k) where k is the length of the slice.
Example: lst[start:end].

Concatenation: O(k) where k is the length of the list being concatenated.
Example: lst1 + lst2.'''