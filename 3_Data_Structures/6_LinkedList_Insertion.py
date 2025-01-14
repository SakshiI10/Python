# Insertion in Linked List:

class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None
    
    def insertAtBegin(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # Check if the list is empty
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node 
        else:
            # If the list is not empty, set the new node's next to the current head
            new_node.next = self.head
            # Update the head to be the new node
            self.head = new_node
    
    def insertAtIndex(self, data, index):
        # If the index is 0, use the insertAtBegin method
        if index == 0:
            self.insertAtBegin(data)
            return

        # Initialize position and current node
        position = 0
        current_node = self.head
        
        # Traverse the list until the position just before the desired index
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        # If the current node is not None, insert the new node at the index
        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def insertAtEnd(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return
        
        # Traverse the list to the last node
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        # Set the next of the last node to the new node
        current_node.next = new_node

    def printList(self):
        # Initialize the current node to the head of the list
        current = self.head
        # Traverse the list and print each node's data
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list

if __name__ == "__main__":
    # Create an instance of LinkedList
    ll = LinkedList()
    ll.insertAtBegin(3)
    ll.insertAtBegin(5)
    ll.insertAtBegin(7)
    ll.printList()

    ll.insertAtIndex(10, 0)  
    ll.insertAtIndex(15, 2)  
    ll.insertAtIndex(20, 5)  
    ll.printList()

    ll.insertAtEnd(30)
    ll.insertAtEnd(35)
    ll.printList()

'''
Time Complexities:
1. Insertion at the Beginning: O(1)
2. Insertion at the Middle: O(n)
3. Insertion at the End: O(n)'''