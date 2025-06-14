''' 
Variable
1. It is used to store a value in it.

2. Scope:
A variable is only available from inside the region it is created, this is called as scope.
a) Global scope
b) local scope

3. Local scope:
A variable created inside a function is available inside that function.
'''
print("Local")
def f1():
    a=100
    print("Local var:",a)
f1()
''' 
Inner function:
The variable a is not available outside the function, but it is available for any function inside the function.
'''
print("Inner")
def f2():
    b=200
    def inner_f2():
        print("Inner var:",b)
        inner_f2()
f2()

''' 
4. Global scope:
A variable created inside a function is available inside that function.
'''
print("Global")
def f3():
    c=300 
    print("Global var:",c)
f3()

''' 
5. Naming Variables
If you operate with the same variable name inside and outside of a function.
a) Global scope
b) Local scope

6. Python support two types of variables:
a) Global Variables
b) Local variables
'''
print("Prac1")
e=10
def fn1():
    e=11
    print(e)
def fn2():
    print(e)
fn1()
fn2()

''' 
Local Variable: Variables which are declared inside a function are called local variables (Eg, e=11).
Global Variable: Variables which are declared on top or using global keyword are called global variables.(Eg, e=10) in above code.
'''
print("Prac2")
f=10
def fn3():
    global f # Here, f changed globally
    f=12
    print(f)
def fn4():
    print(f)
fn3()
fn4()

''' 
If global variable and local variable have the same name then we can access global variable inside a function.
'''