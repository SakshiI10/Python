# Check whether entered number is singledigit even number.

n=int(input("Enter a number: "))
if n in (2,4,6,9):
    print("Single digit Even number")
else:
    print("It is not a single digit even number")