'''
Recursion:
a. Recursive function are a type of function that deals with itself. Function calls itself until some condition stops it.
'''

# Factorial Function:
def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

num=int(input("Enter number: "))
f=fact(num)
print(f)