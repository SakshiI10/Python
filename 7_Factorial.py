#Input a number and compute its factorial.

n=int(input("Enter a number: "))
f=1
if n<0: 
    print("Negative number")
elif n==0:
    print("The factorial is 0")
else:
    for i in range(1, n+1):
        f=f*i;
    print("The factorial is",f)