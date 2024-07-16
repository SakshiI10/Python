# Iterating over dictionaries using for loops
my_dict={"name": "Sakshi", "Age": 30, "CIty": "New York"}
print("Iterating over keys: ")

for key in my_dict:
    print(key)
    
print("\nIterating over values: ")
for value in my_dict.values():
    print(value)
    
print("\nIterating over items: ")
for key, value in my_dict.items():
    print(key,":",value)

# Genrating and Printing a Dictionary
n=5
result_dict={}
for i in range(1, n+1):
    result_dict[i]=i*i
print(result_dict)

# Creating and displaying all combinations of letters in a dictionary. 
data={'1':['a','b'], '2':['c','d']}
keys=list(data.keys())
values=list(data.values())

for i in range(len(values[0])):
    for j in range(len(values[1])):
        print(values[0][i]+values[1][j])
        
# Matching key values in two dictionaries
dict1 = {'key1':1, 'key2':2, 'key3':3}
dict2 = {'key1':1, 'key2':2}
for key in dict1:
    if key in dict2 and dict1[key]==dict2[key]:
        print(f"{key}:{dict1[key]} is present in both x and y")