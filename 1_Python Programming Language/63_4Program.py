# Write a python program to create a shallow copy of sets. 
import copy

original_set={1,2,3,4,5}
shallow_copy=original_set.copy()

original_set.add(6)

print(original_set)
print(shallow_copy)

deep_copy=copy.deepcopy(original_set)
deep_copy.add(7)
print(original_set)
print(deep_copy)