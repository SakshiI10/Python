# Sorting names

st=input("Enter name: ")
namelist=st.split()
namelist.sort()
print("The sorted names are: ")
for name in namelist:
    print(name)