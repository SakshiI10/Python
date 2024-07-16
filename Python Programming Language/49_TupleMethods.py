''' 
1) In Python, methods that add items or remove items are not available with tuple.
Following two methods are available:
a) count()
b) index()

2) count: The count() method returns the number of times a specified value appears in the tuple.
Syntex: tuple.count(value)
'''

t = ('Hello', 24, 12.5, 24, 456, 75, 24)
print(t.count(24))

''' 
3) index(): Searches the tuple for a specified value and returns the position of where it was found.
Syntex: tuple.index(value)
'''

t2 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
i=t2.index('c')
print(i)

''' 
4) Varios operations that we can perform on tuples are very similar to lists.

5) Concatenation of Tuples: The + operator returns a tuple containing all the elements of the first and the second tuple object.
'''

t3 = (1, 2, 3)
t4 = (4, 5, 6)
t5 = t3+t4
print(t5)

''' 
6) Multiply Tuples: The * operator multiplies copies of the same tuple.
'''

t6 = (7, 8, 9)
print(t6*4)

''' 
7) Membership Operations on Tuple
a) IN Operator: The IN Operator returns true if an item exists in the given tuple.
b) NOT IN Operator: The not in operator returns true if an item does not exist in the given tuple.
'''
