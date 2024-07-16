''' 
Dictionary Methods:
1. all()
Return True if all keys of the dictionary are True or if the dictionary is empty.

2. any()
Return True if any key of the dictionary is true. If the dictionary is empty, return False.

3. len()
Return the length the number of items in the dictionary.

4. sorted()
Return a new sorted list of keys in the dictionary.
sorted(iterable, key=None, reverse=False)

5. keys()
Returns a new object of the dictionary's keys.
dictionary.keys()

7. values()
Returns a new object of the dictionary's values.
dictionary.values()
'''

student_details={1: "abc", 2: "def", 3: "ghi"}
print(all(student_details))
print(any(student_details))
print(len(student_details))
print(sorted(student_details))
print(student_details.keys())
print(student_details.values())