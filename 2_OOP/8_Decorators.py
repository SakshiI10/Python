'''
Decorators:
A decorator is just a function that takes another function as an argument and extends its behaviour without explicitly modifying it.

It adds a new functionality to a function.

Functions are taken as the argument into another function and then inside the wrapper function.

Multiple decorators can also be chained in Python.
'''

def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor

def num():
    return 10
print(num())