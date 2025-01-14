# Insertion in stack
print("Insertion")
class Stack:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_full(self):
        return len(self.items) >= self.max_size

    def push(self, item):
        if self.is_full():
            print("Stack is full. Cannot push item.")
        else:
            self.items.append(item)

stack = Stack(max_size=3)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.items)
stack.push(40)  


# Deletion in stack
print("\nDeletion")
class Stack:
    def __init__(self, items):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop item.")
            return None
        return self.items.pop()

stack = Stack([1, 2, 3])
print(stack.pop())  
print(stack.pop())  
print(stack.pop())  
print(stack.pop())  

'''
Time Complexities:
1. Insertion: O(1)
2. Deletion: O(1)
3. Peek/Top: O(1)
4. is_empty/is_full: O(1)
5. Size/Length: O(1)
6. Clear: O(n)
7. Contains/Search: O(n)
8. Print/Display: O(n)
'''