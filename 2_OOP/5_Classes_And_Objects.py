'''
1. Classes:
a. Python reserved keyword "class" is used to create class.

b. Class contains class attributes (These are the properties defined as variable declaration by assigning value) and class methods (These reflects behaviour or description of object).

c. Syntax:
    class classname:
        attribute_definition
        method_definition
    object=classname();

    


2. Objcts:
a. An object is an instance of a class.




3. Relationship between Classes and Objects:
a. Create a class first, which serves as the blueprint.
b. Use the class to create objects (instances).
c. Hence, Multiple objects can be created from a single class, each with its own data.
'''

# Here, class contains data and attribute
class Dog:
  # Attributes (data): These attributes represent the data that each dog object will hold.
  breed = ""
  age = 0

  # Methods (functions)
  def bark(self):
    print(self.breed)

# Create objects (instances) of the Dog class
dog1 = Dog()
dog1.breed = "Labrador"
dog1.age = 3

dog2 = Dog()
dog2.breed = "Poodle"
dog2.age = 1

# Call methods on the objects
dog1.bark()  
dog2.bark()  
