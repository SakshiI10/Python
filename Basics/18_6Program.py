# Print n terms of Fibonacci series.
n=int(input("Enter a number: "))
n1=0
n2=1
print(n1)
print(n2)
count=3
for i in range(count, n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    count+=1