''' 
Creating Dictionary:
Dictionary keys are case sensitive, the same name but different cases of key will be treated distinctly.
'''

d1={'a': 1, 'b': 2, 'c':3}
d2={'A': 1, 'B': 2, 'C':3}
print(d1)
print(d2)

d3={"India": "Delhi", "Italy": "Rome", "Australia": "Canberra"}
print(d3)

# Keys and values both are of string type. We can also have keys and values of different data types.

# Creating Empty Dictionary
d4={}
d5=dict()
print(d4)
print(d5)

d6={1: "one", 2: "two", 3: "three"}
print(d6)

# To access data from the dictionary we use the keys to access their corresponding values. 
d={100: 'abc', 200: 'def', 300: 'ghi'}
print(d[100])
