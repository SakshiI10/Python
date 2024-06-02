''' 
Functions:
1. If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.

2. Define these statements as a single unit and we can call that unit any number of times based on our requirement without rewriting.

3. Functions are known as methods, procedures, subroutines, etc.

4. Python supports 2 types of functions:
a. Built in Functions
Functions which comes along python software.
Eg. id(), type(), input() and eval()
b. User defined Functions
Functions which are developed by a programmer.

# 5. We can create a function:
def function_name(parameters)
"""doc string"""
----------------
return value
'''

# Eg of function without parameter
def great():
    #first function 
    print("Hello WOrld!")
great()
    
# Eg of function with parameter
def my_function(msg):
    #function with paramter
        print(msg)
my_function("Hi")

def greet2():
    print('Inside')
greet2()
print("Outside")