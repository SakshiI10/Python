'''
Abstraction:
1. This means hiding the complexity and only showing necessary features of an object.

2. Data Abstraction = Data Encapsulation + Data hiding

3. Implementation techniques:
a. Functions: Functions are the building blocks of abstraction. They encapsulate a specific task, hiding the internal steps from the user who only interacts with the function's inputs and outputs.

b. Classes and objects: Classes serve as blueprints for creating objects. Abstraction comes into play through:

i. Methods: Methods define functionalities within a class. You can choose to expose only the necessary methods publicly (accessible from outside the class) while keeping internal helper methods private (accessible only within the class).

ii. Abstract classes: These are classes that define a blueprint for behavior but don't provide complete implementations. Subclasses inherit from abstract classes and must implement the missing functionalities. This enforces a common interface for related objects while allowing specific implementations for different scenarios.
'''

class Animal:
    """
    This abstract class represents a generic animal with an abstract method 'make_sound'.
    Subclasses must implement this method to define the specific sound of each animal.
    """

    def __init__(self, name):
        self.__name = name  # Private attribute for animal's name.

    def get_name(self):
        """Public method to access the animal's name (encapsulation)."""
        return self.__name

    def make_sound(self):
        """
        Abstract method that defines the sound-making behavior but requires implementation in subclasses (abstraction).
        """
        raise NotImplementedError("Subclasses must implement the make_sound method")

class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    Implements the make_sound method to define a dog's bark.
    """

    def make_sound(self):
        """Overrides the abstract method to make a dog bark (abstraction)."""
        print(f"{self.get_name()} barks: Woof!")

class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    Implements the make_sound method to define a cat's meow.
    """

    def make_sound(self):
        """Overrides the abstract method to make a cat meow (abstraction)."""
        print(f"{self.get_name()} meows: Meow!")

# Create animal objects (cannot instantiate Animal directly due to the abstract method)
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Access the name using the public getter method (encapsulation)
print(dog.get_name())  # Output: Buddy
print(cat.get_name())  # Output: Whiskers

# Make the animals make sounds using their specific implementations (abstraction)
dog.make_sound()  # Output: Buddy barks: Woof!
cat.make_sound()  # Output: Whiskers meows: Meow!
