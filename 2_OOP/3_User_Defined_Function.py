'''
1. Keyword def followed by paranthesis() is used to define user-defined function.

2. Parathesis() contains
'''
def square(n):
    return n 

def cube(n):
    return square(n)*n

n=5
print("Number: ",n)
print("Square: ",square(n))
print("Cube: ",cube(n))