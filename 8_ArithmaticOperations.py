# Input two integers and code for arithmatic operator and perform operation accordingly.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter Code 1.Add, 2.Sub, 3.Mul, 4.Div, 5.Mod: "))
r=0
if c==1:
    r=a+b
elif c==2:
    r=a-b
elif c==3:
    r=a*b
elif c==4:
    r=a/b
elif c==5:
    r=a%b
else:
    print("Invalid input")
print("Answer is:", r)