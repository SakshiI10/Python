''' 
Dictionary Functions
1. dict()
This function is used to create a dictionary.
TO create empty dictionary: d=dict()
It creates dictionary with specified elements as well.
'''
d=dict([(1, "abc"), (2, "def"), (3, "ghi")])
print(d)

''' 
2. get()
To get the value associated with the key.
d.get(key)
'''
#print(d.get(1))               

''' 
3. pop()
It removes the entry associated with the specified key and returns the corresponding value if the specified key is not available then we will get KeyError
'''
#print(d.pop(3))
            
''' 
4. popitem()
It removes an arbitrary item(key-value) from the dictionary and returns it.
'''
#print(d.popitem())

''' 
5. keys()
It returns all keys associated with the dictionary.
'''
print(d.keys())
for k in d.keys():
    print(k)
    
''' 
6. values()
It returns all values associateed with the dictionary.
'''
print(d.values())
for k in d.values():
    print(k)

''' 
7. items()
It returns list of tuples representing key-value pairs.
[(k,v), (k,v), (k,v)]
'''
for k,v in d.items():
    print(k, "-", v)

''' 
8. copy()
To create exactly duplicate dictionary(cloned copy).
d1=d.copy()

9. setdefault()
If the key is already available then this function returns the corresponding value.
d.setdefault(k,v)
If the key is not available then the specified key-value will be added as new item to the dictionary.
'''
print(d.setdefault(4, "jkl"))
print(d)

