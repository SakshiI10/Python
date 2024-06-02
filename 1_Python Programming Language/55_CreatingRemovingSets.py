''' 
1. Creating Empty set:
Empty curly braces{} will make an empty dictionary in Python.
'''
s1={}
print(type(s1)) # This is incorrect

# To make a set without any elemets, we use the set{} function without any argument.

s2=set()
print(type(s2))

# We can't access or change an element of a set using indexing or slicing. Set data type doesn't not support it.
s3={10, 20, "python", "everyone", 40}
# print(s3[0])  # 'set' object is not subscirptable

''' 
2. Add Items to Set
Once a set is created, you can't change its items, but you can add new items.
a) add(): We can add a single element using the add() method, and multiple elements using the update() method.
'''
s4={1,2,3,4}
s4.add(5)
print(s4)

''' 
b) update()
To add items from another set into the current set, use the update() method.
The update() method can take tuples, dict, lists, strings or other sets as its argument.
In all cases, duplicates are avoid.
'''
s4.update([5,6,7,8])
print(s4)

''' 
c) remove()
We can remove items from sets using different methods.
remove(), discard(), pop(), clear(), del
'''
s4.remove(4)
print(s4)

''' 
d) discard(): Leaves a set unchanged if the element is not present in the set.
'''
s4.discard(3)
print(s4)

# remove(): Raise an error in such a condition(if element ois not present in the set).

# pop(): The pop() is an inbuilt method in python that is used to pop out or remove the elements one by one from the set. The element that is the smallest in the set is removed first followed by removing elements in increasing order. 
s4.pop()
print(s4)

''' 
clear(): The clear() method empties the set.
s4.clear()
print(s4)
''' 

''' 
Del: The ddel keyword will delete the set completely. 
del s4
print(s4)
'''