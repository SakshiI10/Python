''' 
Arguments:
Supporse we have a function f1 with arguments as a and b, and we can call a function with 10 and 20 as an argument.
'''
def func1(a, b):
    c=a+b
    print(c)
func1(10, 20)

''' 
Types of Arguments:
1. Default Arguments:
A default argument is a kind of parameter that takes as input a default value if no value is supplied for the argument when the function is called.
'''
def fun2(n1, n2=30):
    n3=n1+n2
    print(n3)
fun2(40)

''' 
2. Keyword Arguments
A keyword argument is an argument value, passed to function proceeded by the variable name and an equals sign.
Here, order of arguments does not matter but number of arguments must match.
'''
def func3(name, surname):
    print("Hello", name, surname)
func3(name="abc", surname="def")

'''
3. Required/Positional Arguments
The arguments given to a function while calling in a pre-defined positional sequence are required arguments.
If we change the order, then the result may change. 
If we change the number of arguments, then error will occur.
'''
def func4(n4, n5):
    print("Num1 is:", n4)
    print("Num2 is:", n5)
func4(60, 50)

'''
4. Variable Length Arguments
We can use special characters in Pyton functions to pass as many arguments as we want in a function.
Two types of characters:
*args:These are non-keyword arguments
**kwargs:These are keyword arguments
'''
def addition(*nums):
    total=0
    for num in nums:
        total=total+num
    print("Sum is: ", total)
addition(70,80)
addition(70)
addition(71, 72, 73, 74, 75)

def mykwargs(**kwargs):
    for key,value in kwargs.items():
        print(key,"=",value)
mykwargs(first="abc", mid="def", last="ghi")
''' 
There are several methods that have no arguments, while many have a large number of arguments.
'''