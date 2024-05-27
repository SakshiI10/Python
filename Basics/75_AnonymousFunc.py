''' 
Anonymous Function:
Anonymous function is function which doesn't have any name.

The lambda keyword is used to define an anonymous function in Python.

The purpose of anonymous function is just for instant use.

Use lambda functions wherever function objects are required.

Lambda functions are syntactically restricted to a single expression.
s=lambda a,b:a+b
'''

#Find sum of 2 numbers without lambda function.
def sum(a,b):
    return a+b
print(sum(10,20))

#Find sum of 2 numbers with lambda function.
s=lambda a,b:a+b
print("The Sum: ",s(10,20))

''' 
A lambda is a special type of function without the function name.

We use the lambda keyword instead of def to create a lambda function.

f=lambda a:a*a
f=function object that accepts and stores the result of the expression
lambda=keyword
a=argument
a*a=one line expression

Eg, To execute a lambda function, we need to call it. This lambda function doesn't have any argument.
'''
msg=lambda:print("Hello World!")
msg()
''' 
Lambda function with an argument
Similar to normal function, a lambda function can also accept arguments.
'''
msg2=lambda name:print("Hey there!,", name)
msg2('Python')
''' 
Lambda function internally returns expression value and we are not required to write return statement explicitly.

Sometimes, we can pass function as argument to another function. In such cases lambda functions are best choice.
'''