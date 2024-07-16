# Print alternate character in uppercase

st=input("Enter string: ")
l=len(st)
print("Original string is: ",st)

st2=""
for a in range(0,l,2):
    st2+=st[a]
    if a<(l-1):
        st2 += st[a+1].upper()
print("Alternatively captalised string is: ",st2)