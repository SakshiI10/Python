#Input a number and coputer its factorial.

n=int(input("Enter a number: "))
f=1
if n<0:
    print("Factorial of negative number doesn't exist")
elif (n==0):
    print("Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        f=f*i
    print("The factorial is:",f)