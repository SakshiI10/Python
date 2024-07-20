'''
Inheritance:
1. It is the process of deriving new classes(subclasses, derived classes, or child classes) the existing classes  (superclasses, base classes, or parent classes).

2. a. Base Class: The original class that defines the properties and methods that will be inherited.

b. Subclass: The new class that inherits properties and methods from the base class. It can also add its own unique features.

3. Syntax:
class base_class:
    pass
class derived_class(base_class):
    pass
    
a. In child class, the name of the parent class appears in paranthesis.

b. It is important that the base class and the derived class must be defined in the same scope.

4. Functions used
a. issubclass()
It returns True if the specified object is a subclass of the specified object, otherwise retuns False.

b. super()
This function helps in accessing function of the super class into it's child class.
Super class methods are inherited in child class, but cannot be used directly.
It access parent class with dot membership operator without using name of the parent class.'''

# Inheritance structure
class circle:
    pass
class Sphere(circle):
    pass

x=issubclass(Sphere, circle)
y=issubclass(circle, Sphere)
print(x)
print(y)

# Accessing parent class member in child class
class base:
    def __init__(self, a):
        self.a=a

class derived(base):
    def __init__(self, x, y):
        base.a=x
        self.b=y
    def print_sum(self):
        self.s=base.a+self.b
        print("Sum:",self.s)

d=derived(1, 2)
d.print_sum()

'''
5. Inheritance reflects IS-A relationship among classes.
'''