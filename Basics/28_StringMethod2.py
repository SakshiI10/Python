# 22) format()
print("{} is a {}".format("Mango","Fruit"))
print("{1} is a {0}".format("Mango","Fruit"))
z="{0}, {1}, {2}, {3}"
print(z.format(*"5678"))

# 23) join()
j="*"
print(j.join("abcd"))

# 24) swapcase()


# 25) splitlines()

# 26) maketrans()
# 27) translate()
source="abcdefgh"
target="12345678"
trans_table=str.maketrans(source,target)
code="dad has cad".translate(trans_table)
print(code)

# 28) replace()
deg="B Tech"
print(deg.replace('B','M'))

c='INDIAN'
# 29) find()
print(c.find('I'))
print(c.find('I', 1, 6))

# 30) rfind()
print("sakshi".rfind('s'))

# 31) index()
print(c.index('A'))

# 32) rindex()
print("sakshi".rindex('s'))


# 33) ljust()
print("abc".ljust(10,"*"))

# 34) rjust()
print("abc".rjust(10,"*"))


# 35) partition()
print("Programming".partition("ram"))

# 36) rpartition()
print("Programming".rpartition("ram"))

# 37) strip()
# 38) lstrip()
# 39) rstrip()

# 40) split()
# 41) rsplit()

# 42) zfill()