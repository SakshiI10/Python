'''
init Function:
1. The __init__ function, also known as the constructor, is a special method in Python classes that automatically initializes new object instance.

2. It is called whenever a new object is created from a class.

3. Every class has in-built __init__() function, it assigns values to object properties.

4. The first parameter of a method is self.

5. The self parameter is reference to the current instance of the class, self refers to that exact object inside the class methods.
'''

class Student:
    '''This class represent a student with attribues Roll No., Name and Marks and a method to print it'''

    def __init__(self, rollno, name, marks):
        '''This is the constructor method that initializes a new student object. It takes three arguments: rollno, name and marks.'''
        self.rollno = rollno
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll Number: ", self.rollno)
        print("Name: ", self.name)
        print("Marks: ", self.marks)

# Create Student Objects
s1 = Student('10', 'Sakshi', '84.08')

# Call the display method on each object
s1.display()

class Sample:
    def display(self):
        print(self)

s = Sample()
s.display()
