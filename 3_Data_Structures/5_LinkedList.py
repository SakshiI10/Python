'''
1. A linked list is a type of linear data structure similar to arrays. 

2. It is a collection of nodes that are linked with each other. A node contains two things first is data and second is a link that connects it with another node.

3. Our first node is where head points and we can access all the elements of the linked list using the head.

4. Creating a Linked List: 
We have created a Node class in which we have defined an __init__ function to initialize the node with the data passed as an argument and a reference with None because we have only one node.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
