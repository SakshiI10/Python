'''
Polymorphism:
1. This is the concept of using common operation in difference ways for difference data input.

2. When function with same name are used for difference data types they are called polymorphic functions.

3. Types of Polymorphism:
a. Compile time Polymorphism
b. Run time Polymorphism 
'''

#a. Compile time Polymorphism:
#i. Operator Overloading: Operator overloading allows the same operator to have different meanings based on the context. In Python, this is done by defining special methods in a class, such as __add__ for the + operator.
class Rectangle:
    def __init__(self, width, height):
        self.width = width  # Initialize the width attribute
        self.height = height  # Initialize the height attribute

    # Overloading the + Operator
    def __add__(self, other):
         return Rectangle(self.width + other.width, self.height + other.height)
    
    def __str__(self):
        # Provide a string representation of the Rectangle object
        return f"Operator Overloading: Rectangle(width={self.width}, height={self.height})"

# Create two Rectangle objects
rect1 = Rectangle(3, 4)
rect2 = Rectangle(5, 6)

# Add the two Rectangle objects using the overloaded + operator
rect3 = rect1 + rect2

# Print the result
print(rect3)  # Output: Rectangle(width=8, height=10)




# ii. Method Overloading: Method overloading allows multiple methods in a class to have the same name but different parameters (different type or number of parameters). 
class MathOperations:
    # Define the add method with method overloading capability using default arguments
    def add(self, *args):
        total = 0
        for num in args:
            total += int(num)  # convert to int
        return total

# Create an instance of MathOperations
math_ops = MathOperations()
print("Method Overloading:", math_ops.add(1, 2))
print("Method Overloading:", math_ops.add(1, 2, '3', 4))




# b. Run time Polymorphism:
# i. Duck Typing: Duck typing is a form of polymorphism that focuses on whether an object can perform the required operations (methods and properties) rather than its explicit type. It is based on the principle: “If it looks like a duck and quacks like a duck, it probably is a duck.”

# Define the Bird class with a method `fly`
class Bird:
    def fly(self):
        return "Bird is flying in the sky" 

# Define the Airplane class with a method `fly`
class Airplane:
    def fly(self):
        return "Aeroplane is in the sky" 

# Define a function that takes any object with a `fly` method
def let_it_fly(entity):
    return entity.fly() 

# Create an instance of the Bird class
bird = Bird()
# Create an instance of the Airplane class
airplane = Airplane()

print(let_it_fly(bird))
print(let_it_fly(airplane)) 




# ii. Method Overriding: Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method to be executed is determined at runtime based on the object’s actual type.
class base():
    def method(self):
        print("I'm in base")
    
class middle(base):
    def method(self):
        print("I'm in middle")
        super(middle,self).method()

class derived(middle):
    def method(self):
        print("I'm in derived")
        super(derived, self).method()
d=derived()
d.method()
