# List Methods:

# 1) append(): Adds x to the end of the list as a single element.
days=["Mon", "Tue", "Wed"]
print(days)
days.append("Thu")
print(days)

# 2) extend(): it iterates over the given iterable (like a list, tuple, or string) and adds each of its elements individually to the list.
months=["Jan", "Feb"]
months.extend(["Mar"])
print(months)

# 3) insert(): Inserts x at index i, shifting elements to the right.
n=[0, 1, "two", 4, "five", 6, 7, 8, "nine"]
n.insert(3, "three")
print(n)

# 4) remove(): Removes the first occurrence of the specified value.
n.remove(1)
print(n)

# 5) pop(): Removes and returns the element at the given index, when no index is given, it removes and returns the last element from the list by default.
n.pop()
print(n)
n.pop(1)
print(n)

# 6) clear()
odd=[1, 3, 5, 7, 9]
odd.clear()
print(odd)

#7) index()
name=['abc', 'def', 'ghi', 'jkl', 'mno']
print(name.index('abc'))

# 8) cound()
myname='sakshi'
print(myname.count('s'))

# 9) sort or sorted()
alpha=['qqq', 'www', 'eee', 'rrr', 'ttt']
alpha.sort()
print(alpha)

# 10) reverse()
alphabets=['qqq', 'www', 'eee', 'rrr', 'ttt', 'yyy']
alphabets.reverse()
print(alphabets)

# 11) copy()
num=[1, 2, 3, 4, 5]
copied=num.copy()
print(copied)

# 12) Len()
print(len(copied))

# 13) List()
print(list())
print(list([]))
print(list([1, 2, 3]))
print(list(myname))
t=("This", "is", "Tuple")
print(list(t))
s={"This", "is", "Set"}
print(list(s))

# 14) Max()
print(max(num))
print(max([1,2,3], [4,5,6]))

# 15) Min()
print(min(num))
print(min([1,2,3], [4,5,6]))

# 16) range()
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))