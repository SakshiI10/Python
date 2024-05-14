''' 
Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference. 

1. Set union: Union of A and B is a aset of all elements from both sets.
Performed Using:
| operator
union()
'''
s1={1,2,3}
s2={1,2,3,4,5,6,7,8,9}
print(s1.union(s2)) #print(s1|s2)

''' 
2. Intersection of A and B is a set of elements that are common in both the sets.
Performed using:
& operator
intersection()
'''
print(s1.intersection(s2)) #print(s1&s2)

''' 
3. Set difference: Difference of the set B from set A(A-B) is a set of elements that are only in A but not in B.
Performed using:
- operator
difference()
'''
print(s2.difference(s1)) #print(s2-s1)

''' 
4. Set difference of A and B is a set of elements in A and B but not in both.
Performed Using:
^ operator
symmetric_difference()
'''
print(s2.symmetric_difference(s1)) #print(s2^s1)

''' 
5. difference(): Returns a set containing the difference between two or more sets. Method returns a new set, without the unwanted items.
'''

''' 
6. difference_update(): Removes the items in this set that are also included in another, specified set. Method removes the unwanted items form the original set.
'''

''' 
7. intersection(): Returns a set, that is the intersection of two or more sets. Method returns a new set, without the unwanted items.
'''

''' 
8. intersection_update(): Method removes the unwanted items from the original set.
'''

''' 
8. Removes the items in this set that aren't present in other, specified set(s).
'''
