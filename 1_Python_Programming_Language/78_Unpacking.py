# List Unpacking
a, b, c = [10, 20, 30]
print(a + b + c)

# Tuple Unpacking
t = (40, 50, 60)
a, b, c = t
print(a, b, c)
print(a + b + c)

t = (1, (2, 3), 4)
a, (b, c), d = t
print(b, c)

