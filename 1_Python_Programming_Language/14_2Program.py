# Input 3 numbers and find largest.

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=int(input("Enter third number: "))
if (n1>=n2) and (n1>=n3):
    print(n1,"is largest")
elif (n2>=n1) and (n2>=n3):
    print(n2,"is largest")
else:
    print(n3,"is largest")
    