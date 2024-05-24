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

#