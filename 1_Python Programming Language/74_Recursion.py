''' 
Recursion:
Recursion is the process of defining something in terms of itself.

A recursive functin that calls itself, again and again.

def recursive():
    recursive():
recursive()
'''
def factorial(num):
    if num==1:
        return 1
    elif num==0:
        return 1
    else:
        return num*(factorial(num-1))
print("Factorial is:", factorial(6))

''' 
Each recursive function must have a base condition that stops the recursive or else the function calls itself infinitely.

The max depth of recursion is 1000. If the limit is crossed it results in Recursion error.
'''