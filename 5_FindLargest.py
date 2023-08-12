# Input 3 numbers and find largest.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b & a>c:
    print(a,"is greater")
elif b>c:
    print(b,"is greater")
else:
    print(c,"is greater")