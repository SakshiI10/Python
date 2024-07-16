# Sorting a dictionary by value
mydict={'abc':1, 'ghi':3,'def':2,'jkl':4,'mno':5}
mykeys=list(mydict.keys())
mykeys.sort()
sorted_dict={i:mydict[i] for i in mykeys}
print(sorted_dict)

# Adding a key to a adictionary
my_dict={0: 19, 1:20}
my_dict[2]=30
print(my_dict)

# Concatenating Dictionaries to create a new one
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
result_dict={}
for d in [dict1, dict2, dict3]:
    result_dict.update(d)
print(result_dict)

# Checking if a given key already exists in a dictionary
my_dict={"name": "Sakshi", "Age": 30, "CIty": "New York"}
key="name"
if key in my_dict:
    print(f"{key} already exists in the dictionary")
else:
    print(f"{key} does not exists in the dictionary")