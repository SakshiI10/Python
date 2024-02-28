# String Statistics

st=input("Enter string: ")
l=u=d=s=p=0
for a in st:
    if a.islower():
        l+=1
    elif a.isupper():
        u+=1
    elif a.isdigit():
        d+=1
    elif a.isspace():
        s+=1
    elif a.isprintable():
        p+=1

print("Statistics: ")
print(l, "lowercase letters")
print(u, "uppercase letters")
print(s, "spaces")
print(d, "digits")
print(p, "delimeters")