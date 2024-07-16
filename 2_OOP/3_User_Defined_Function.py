'''
1. Keyword def followed by paranthesis() is used to define user-defined function.

2. Parathesis() contains function arguments.

3. Syntax:
    def function_name(arguments):
        statement(s)

4. Function name should be unique and function arguments are the values that are passsed to function body.

5. Scope and Life of Variable:
a. Local:
i. Scope: inside a function
ii. Life: Period throughout which variable exists

b. Global:
i. Scope: Throughout the funstion
ii. Life: Entire Execution

6. Docstring
__docstring__ attribute: Availability
function_name.__doc__: Access

7. Returning Value
a. The return statement returns control and value to calling function.

b. If no result to return, then function returns None value.

c. Function can contains one or more return statements.

d. Function can return numeric value, list, tuple, or a dictionary.
'''

def square(n):
    return n 

def cube(n):
    return square(n)*n

n=5
print("Number: ",n)
print("Square: ",square(n))
print("Cube: ",cube(n))