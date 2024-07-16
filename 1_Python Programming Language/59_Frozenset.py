''' 
Frozenset:
Frozenset is a new class that has characteristics of a set, but its elements cannot be changed once assigned.

Tuples=Immutable lists
Frozensets=Immutable sets

Sets being mutable are unhashable, so they can't be used as dictionary keys.
'''
key={'student', 'name'}
#dict_val-{key: 'lily', 'marks':92} #using set as a key

''' 
Frozenset method():
copy()
issubset()
difference()
issuperset()
intersection()
symmetric_difference()
isdisjoint()
union()

Frozenset being immutable, it doesn't have methods that add or remove elements.
'''
A=frozenset([1,2,3,4])
B=frozenset([3,4,5,6])
print(A.isdisjoint(B))
print(A.difference(B))
