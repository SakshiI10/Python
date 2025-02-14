# Concept 1: Lists inside a tuple can be edited but tuple can't.

siblings_ids = (1, 2, [3, 4], 11, 9)

siblings_ids[2].append(5)  # Modifies the list at index 2
print(siblings_ids)  # Output: (1, 2, [3, 4, 5], 11, 9)
siblings_ids[4] = 10  # Modifies the list at index 2
print(siblings_ids)  # Output: (1, 2, [3, 4, 5], 11, 9)
