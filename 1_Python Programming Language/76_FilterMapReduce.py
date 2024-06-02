''' 
Filter
It allows to write simpler and shorter code, without necessary needing to bother about complexity like loops and branching.

We can use lambda functions very commonly with filter() because this function accepts functin as argument.

We can use filter() to filter values from the given sequences based on some condition.

Syntax: filter(function, sequence)
'''
#Without Lambda
def isEven(l):
    for x in l:
        if x%2==0:
            print(x, end=" ") 
l=[0,5,10,15,20,25,30]
isEven(l)

#With Lambda
l1=list(filter(lambda x:x%2==0,l))
print(l1)


''' 
Map()
For every element present in the given sequence, apply some functionality and generate new element with the required modification.

For this requrement, we should go for map() function.

Syntax: map(function, iterables)

The function can be applied on each element of sequence and generate new sequences.
'''
#without lambda function:
l=[1,2,3,4,5]
def doubleit(x):
    return 2*x
li=list(map(doubleit, l))
print(l1)

#With Lambda
l2=list(map(lambda x:2*x, l))
print(l2)


''' 
Reduce:
Reduces the sequence of elements into a single element by applying the specified function.

syntex: reduce(function, sequence)
'''
import functools
lis=[1,3,5,6,2]
print(functools.reduce(lambda a,b:a+b,lis))
print(functools.reduce(lambda a,b:a if a>b else b,lis))
