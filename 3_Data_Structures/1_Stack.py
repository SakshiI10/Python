'''
Stack:
1. A stack is a fundamental data structure that operates based on the "Last In, First Out" (LIFO) principle.

2. Implementation: 
Stacks can be implemented using List, Linked lists, collection.deque or queue.LifeoQueue. 

3. Real-world examples of stacks:
a. Undo/Redo functionality
b. Function call stack
c. Expression evaluation

4. Operations: 
These are basic operations that manipulate the stack:
a. Push: Adds a new element to the top of the stack.
b. Pop: Removes and returns the top element from the stack.
c. Peek: Returns the top element without removing it (useful for checking the next element to be popped).
d. isEmpty: Checks if the stack is empty.
e. isFull (optional): Checks if the stack is full (relevant for fixed-size stacks).
'''

# Stack as an Abstract Data Type
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Check if the stack is empty.
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)

    def pop(self):
        # Remove and return the item from the top of the stack.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        # Return the item at the top of the stack without removing it.
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        # Return the number of items in the stack.
        return len(self.items)

    def __str__(self):
        # Return a string representation of the stack.
        return str(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushes:", stack)
    print("Top item:", stack.peek())
    print("Popped item:", stack.pop())
    print("Stack after pop:", stack)
    print("Stack size:", stack.size())
