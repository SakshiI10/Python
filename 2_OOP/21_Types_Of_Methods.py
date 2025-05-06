# Instance Method
# a) Default method type in a class.
# b) Takes self as the first parameter, which refers to the current object (instance).
# c) Can access and modify instance variables.
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):  # instance method
        print(f"Hello, my name is {self.name}")

s = Student("Alice")
s.greet()

# 2. Class Method
# a) Declared using @classmethod decorator.
# b) Takes cls as the first parameter, referring to the class, not the instance.
# c) Can access/modify class variables, but not instance variables directly.
class Employee:
    company = "ABC"

    @classmethod
    def get_company(cls):
        return cls.company

print(Employee.get_company())

# 3. Static Method
# a) Declared using @staticmethod decorator.
# b) Takes no self or cls parameter.
# c) Behaves like a regular function, just placed inside a class for organizational purposes.
# d) Cannot access instance or class variables directly.
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(3, 4))


