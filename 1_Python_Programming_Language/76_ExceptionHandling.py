''' 
Errors:
In any Programming Language 2 types of errors are possible:
1. Syntax Errors/Compile time error:
The errors which occurs because of invalid syntax are called syntax errors.

2. Runtime Errors:
A runtime error in a program is an error that occurs when the program is running after being successfully compiled. Runtime errors are called as "bugs" or logical errors or exception.

There are a variety of runtime errors that occur such as:
1. Logical Errors
2. I/O Errors
3. Undefined Object Errors
4. Division by zero errors and many more.

Exception:
An unwanted and unexpected event that disturbs the normal flow of a program is called an exception.

The main objective of exception handling is graceful termination of the program.

Types of Exceptions:
1. ZeroDivisionError:
It is a built-in python exception when a number is divided by 0.

2. TypeError
If you attempt to divide an integer with a string, the data types of the integer and the string object will not be compatible.
'''

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("Division successful!")

finally:
    print("Execution complete.")
