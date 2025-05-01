''' 
We can change the tuple into a list, change the list, and convert the list back into a tuple.
'''

# Change Tuple Values
x = ('cat', 'dog', 'cow')
y=list(x)
y[1] = 'chicken'
x=tuple(y)
print(x)

# Add items
y.append('goat')
x=tuple(y)
print(x)

# Add tuple to tuple
z=('zebra',)    #, is must
x=x+z
print(x)

''' 
Remove Items: We can't remove items from tuple.
''' 
