# Calculate sum of digits in a string

st=input("Enter string: ")
s=0
for char in st[0:len(st)]:
    if char.isdigit():
        s=s+int(char)
print("Sum of digits = ",s)