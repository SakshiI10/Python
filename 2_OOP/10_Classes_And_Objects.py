'''
1. Classes:
a. Python reserved keyword "class" is used to create class.

b. Class contains class attributes (These are the properties defined as variable declaration by assigning value) and class methods (This reflects behaviour or description of object).

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

# Here, class contains attribute and methods.
class Dog:
  # Attributes (data): These attributes represent the data that each dog object will hold.
  breed = ""
  age = 1

  # Methods (functions)
  def bark(self):
    print(self.breed)
    print(self.age)

# Create objects (instances) of the Dog class
dog1 = Dog()

# But the moment you write: dog1.breed = "Labrador" You are overriding the class-level breed attribute just for that object (dog1). Now dog1 has its own breed, different from the class default.
dog1.breed = "Labrador"
dog1.age = 3

dog2 = Dog()
dog2.breed = "Poodle"

# Call methods on the objects
dog1.bark()  
dog2.bark()  

'''
4. When class is defined, no memory is allocated. It is a logical entity that contains attributes and methods.

5. Method is a function defined inside a class, memory is allocated because it contains local variables, arguments and return address.

6. Object is an instantiation of a class, memrory is allocated. It is an encapsulation of variables and functions into a single entity.
'''