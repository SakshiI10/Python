''' 
1. all(): Returns True if all elements of the set are true.

2. any(): Returns True if any element of the set is true. If the set is empty, returns False.

3. enumerate() Returns an enumerate object. It contains the index and value for all the items of the set as a pair.

4. len(): Returns the length in the set.

5. max(): Returns the largest item in the set.

6. min(): Returns the smallest item in the set.

7. sorted(): Returns a new sorted list from elements in the set.

8. sum(): Returns the sum of all elements in the set.
'''

x={1,2,3,4,5,6,7,8,9}
print(len(x))
print(max(x))
print(min(x))
print(sum(x))
print(enumerate(x))
print(all(x))
print(any(x))
print(sorted(x))