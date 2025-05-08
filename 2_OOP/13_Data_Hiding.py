'''
Data Hiding:
1. Data hiding restricts direct access to specific variables (attributes) and methods defined within a class.

2. Advantages:
a. Prevents accidental modification
b. Enhances security
c. Improves code maintainability
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
