# Rotate string character in cyclic order

st=input("Enter string: ")
for i in range(0, len(st)):
    print(st[i:],end="")
    print(st[0:i])