# Count vowels

st=input("Enter string: ")
l=len(st)
v=0
for a in range(l):
    if st[a] in 'aeiou' or st[a] in 'AEIOU':
        v+=1
print("Number of vowels are: ",v)