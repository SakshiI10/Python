# 1) Create list with numbers 0...10
print(list(range(0,11)))

# 2) Create list with odd numbers in 50...100
print(list(range(51, 100, 2)))

# 3) Create list with square 1...10
sq=[n**2 for n in range(1, 11)]
print(sq)

# 4) Create list using Cartesian product of 2 lists
c=[x+y for x in ['a', 'b', 'c'] for y in ['x', 'y', 'z']]
print(c)

# 5) Create list using addition of numbers in 2 lists
a=[x+y for x in [1, 2, 3] for y in [4, 5, 6]]
print(a)

# 6) Create list using multiplication of 2 lists
m=[x*y for x in [1, 2, 3] for y in [4, 5, 6]]
print(m)

# 7) Create list of 2^x for x in 1...10
e=[2**x for x in range(1, 11)]
print(e)