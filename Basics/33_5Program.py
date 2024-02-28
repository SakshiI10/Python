# Remove punctuation characters

punctuation=''' ~!@#$%^&*()_[]{};':",./<>? '''
st1=input("Enter string: ")
st2=""
for char in st1:
    if char not in punctuation:
        st2=st2+char
print(st2)