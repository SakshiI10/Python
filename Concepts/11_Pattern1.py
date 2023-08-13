# Print Fibonacci series.

n=int(input("Enter an integer: "))
n1=0
n2=1
print(n1)
print(n2)
count=3
while count<=n:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    count+=1
