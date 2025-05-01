'''
Encapsulation:
1. Encapsulation in Python is a fundamental concept in OOP that bundles data and methods that work on that data within a single unit, a class.

2. It hides private details of a class from other objects.

3. This prevents user from direct modification of data.

4. Encapsulation helps prevent accidental modification of data by restricting direct access to attributes (variables) within a class.

5. It is usually accomplished by providing two types of methods called getter method and setter method.
a. Getter: It gets the values and do not change values of attributes.
b. Setter: It changes the value of attributes.
'''

# Encapsulation is done by encapsulating the code in a class
class BankAccount:
  def __init__(self, balance):  # Constructor
    self.__balance = balance  # Private attribute and this is data hiding because __ is used.

  def get_balance(self):  # Public method to access balance
    return self.__balance

  def deposit(self, amount):  # Public method to deposit
    self.__balance += amount

# Creating an account object
account = BankAccount(100)

# Public methods can be accessed
print(account.get_balance())  # Output: 100
account.deposit(50)
print(account.get_balance())  # Output: 150

'''
With private method: Others can change it safely, because you control the rules.
Without private method: Others can’t change the private data.
'''