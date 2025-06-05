'''
Aggregation:
1. It is the concept of linking two logically related objects where one object belongs to the other object.

2. It shows a "has-a" relationship.

3. Eg, address object can be related to employee object and student object.

4. Hence, Aggregation in Python refers to a relationship between classes where one class ("has-a" relationship) contains a reference to another class as an instance variable. This allows you to create complex objects by combining simpler ones.
'''

class Student:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def introduce(self):
    print(f"Hi, I'm {self.name} and I live at {self.address}.")

class Course:
  def __init__(self, name, instructor):
    self.name = name
    self.instructor = instructor  # Aggregation: Course has an instructor (Student)

  def get_info(self):
    print(f"{self.name} course taught by {self.instructor.name}")  # Accessing instructor's name

# Create a Student object (We can pass arguments while creating object)
student1 = Student("Alice", "123 Main St")

# Create a Course object (We can paas arguments while creating object)
course1 = Course("Python Programming", student1)

student1.introduce()  # Hi, I'm Alice and I live at 123 Main St.
course1.get_info()    # Python Programming course taught by Alice
