# Input a string and check for palindrome.

st=input("Enter string: ")
l=len(st)
mid=int(l/2)
b=-1
for f in range(mid):
    if st[f]==st[b]:
        f+=1
        b-=1
    else:
        print(st,"is not Palindrome")
        break
else:
    print(st,"is Palindrome")