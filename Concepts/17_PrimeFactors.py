# Print prime factors of a factors.

n=int(input("Enter your numbers: "))
print("Prime factors of",n,"are: ")
i=2
while i<=n:
    if n%i==0:
        print(i, end=" ")
        n=n/i
        continue
    i=i+1
if n>1:
    print(int(n))