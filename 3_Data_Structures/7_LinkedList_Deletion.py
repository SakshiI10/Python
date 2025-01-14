# Deletion in Linked LIst
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def remove_first_node(self):
        """Remove the first node from the linked list."""
        if self.head is None:
            # If the list is empty, there is nothing to remove
            return
        
        # Move the head pointer to the next node
        self.head = self.head.next

    def remove_last_node(self):
        """Remove the last node from the linked list."""
        if self.head is None:
            # If the list is empty, there is nothing to remove
            return
        
        if self.head.next is None:
            # If there's only one node, remove it by setting head to None
            self.head = None
            return

        current_node = self.head
        # Traverse to the second-to-last node
        while current_node.next.next is not None:
            current_node = current_node.next
        
        # Remove the last node by setting the next of the second-to-last node to None
        current_node.next = None

    def remove_at_index(self, index):
        """Remove the node at the specified index from the linked list."""
        if self.head is None:
            # If the list is empty, there's nothing to remove
            return
        
        if index == 0:
            # Remove the first node if index is 0
            self.remove_first_node()
            return

        current_node = self.head
        position = 0

        # Traverse to the node just before the one to be removed
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        # If we found the node to remove, adjust the pointers
        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def remove_node(self, data):
        """Remove the first occurrence of a node containing the specified data."""
        current_node = self.head

        # Check if the head node contains the specified data
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse the list to find the node with the specified data
        while current_node is not None and current_node.next is not None and current_node.next.data != data:
            current_node = current_node.next

        # If the node with the specified data is found, bypass it
        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next

    def display(self):
        """Display the entire list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Create a linked list and manually set nodes
ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)

print("Original list:")
ll.display()  # Output: 1 -> 2 -> 3 -> None

# Remove the first node
ll.remove_first_node()
ll.display()  # Output: 2 -> 3 -> None

# Remove the last node again
ll.remove_last_node()
ll.display()  # Output:2 -> None

# Remove node at index 0
ll.remove_at_index(0)
ll.display() 

# Remove a node with certain data
ll.remove_node(3)
ll.display()  # Output: 1 -> 2 -> 4 -> None