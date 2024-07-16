# 22) format()
print("{} is a {}".format("Mango","Fruit"))
print("{1} is a {0}".format("Mango","Fruit"))
z="{0}, {1}, {2}, {3}"
print(z.format(*"5678"))

# 23) join()
j="*"
print(j.join("abcd"))

# 24) swapcase()
print("New Delhi".swapcase())

# 25) maketrans()
# 26) translate()
source="abcdefgh"
target="12345678"
trans_table=str.maketrans(source,target)
code="dad has cad".translate(trans_table)
print(code)

# 27) replace()
deg="B Tech"
print(deg.replace('B','M'))

c='INDIAN'
# 28) find()
print(c.find('I'))
print(c.find('I', 1, 6))

# 29) rfind()
print("sakshi".rfind('s'))

# 30) index()
print(c.index('A'))

# 31) rindex()
print("sakshi".rindex('s'))

# 32) ljust()
print("abc".ljust(10,"*"))

# 33) rjust()
print("abc".rjust(10,"*"))

# 34) partition()
print("Programming".partition("ram"))

# 35) rpartition()
print("Programming".rpartition("ram"))

# 36) lstrip()
print(" All is Wel".lstrip(),"!")
print("***All is Well***".lstrip("*"))
print("***All is Well***".lstrip("A"))
print("***All is Well***".lstrip("All"))

# 37) rstrip()
print(" All is Wel".rstrip(),"!")
print("***All is Well***".rstrip("*"))
print("***All is Well***".rstrip("A"))
print("***All is Well***".rstrip("All"))

# 38) strip()
print(" All is Wel".rstrip(),"!")

# 39) split()
print("abc-def-ghi-jkl".split('-'))
print("abc-def-ghi-jkl".split('-',2))

# 40) rsplit()
print("abc-def-ghi-jkl".rsplit('-'))
print("abc-def-ghi-jkl".rsplit('-',2))

# 41) splitlines()
print("123\n\n456\n789\n\n".splitlines())

# 42) zfill()
print("abc".zfill(10))