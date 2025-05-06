'''
Types of inheritance:
1. Single Inheritance: A subclass inherits from only one parent class. This is the most common and straightforward type.'''
class base:
    def __init__(self, a):
        self.a = a

class derived(base):
    def __init__(self, a, b):
        super().__init__(a)  # Call base class constructor with x
        self.b = b

    def print_sum(self):
        self.s = self.a + self.b
        print("Sum using Single Inheritance:", self.s)

# Create an object of the derived class
d = derived(1, 2)  # Pass 1 for base.a and 2 for self.b

# Call the print_sum method
d.print_sum()

'''
2. Multilevel Inheritance: A subclass inherits from another subclass, which in turn inherits from a base class. This creates a chain of inheritance.'''
class base:
    def __init__(self, a):
        self.a = a

class intermediate(base):
    def __init__(self, a, b):
        super().__init__(a)  # Initialize base class with a
        self.b = b

class derived(intermediate):
    def __init__(self, a, b, c):
        super().__init__(a, b)  # Initialize intermediate class with a and b
        self.c = c

    def print_sum(self):
        self.s = self.a + self.b + self.c
        print("Sum using Multilevel Inheritance:", self.s)

# Create an object of the derived class
d = derived(1, 2, 3)

# Call the print_all method
d.print_sum()

'''
3. Multiple Inheritance: A subclass inherits from multiple parent classes. This can be trickier to manage as it can lead to ambiguity if both parent classes have methods with the same name.'''
class base1:
    def __init__(self, a):
        self.a=a

class base2:
    def __init__(self, b):
        self.b=b

class derived(base1, base2):
    def __init__(self, a, b):
        base1.__init__(self, a)
        base2.__init__(self, b)

    def find_larger(self):
        if self.a>self.b:
            l=self.a
        else:
            l=self.b
        print("Larger Interger using Multiple Inheritance:",l)

d=derived(10,15)
d.find_larger()

'''
4. Hierarchical Inheritance: Multiple subclasses inherit from a single base class.'''
class Number:  # Base class
    def __init__(self, a):
        self.a = a

class SumCalculator(Number):  # Derived class 1 (inherits from Number)
    def __init__(self, a, b):
        super().__init__(a)  # Call Number's constructor for value1
        self.b = b

    def calculate_sum(self):
        return self.a + self.b

class LargerNumberFinder(Number):  # Derived class 2 (inherits from Number)
    def __init__(self, a, b):
        super().__init__(a)  # Call Number's constructor for value1
        self.b = b

    def find_larger(self):
        return max(self.a, self.b)

# Create objects of the derived classes
calculator = SumCalculator(5, 3)
finder = LargerNumberFinder(10, 7)

# Access methods from derived classes
sum_result = calculator.calculate_sum()
larger_number = finder.find_larger()

print("Sum using Hierarchical Inheritance:", sum_result, "and Larger number:",larger_number) 

'''
5. Hybrid Inheritance
'''
class base1:
    def __init__(self, a):
        self.a=a

class base2:
    def __init__(self, b):
        self.b=b

class Sum_Calc(base1):
    def __init__(self, a, b):
        base1.__init__(self, a)
        base2.__init__(self, b)
        self.c=self.a+self.b
    def print_sum(self):
        # print(self.c)
        pass

class Mul_Calc(base1, base2):
    def __init__(self, a, b, c, d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def print_Mul(self):
        self.s=self.a*self.b*self.c*self.d
        print(self.s)

d1=Sum_Calc(1, 2)
d1.print_sum()
d2=Mul_Calc(d1.a, d1.b, d1.c, 4)
d2.print_Mul()

