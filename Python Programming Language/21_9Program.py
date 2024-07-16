# Print factors of given number.

n=int(input("Enter a number: "))
print("Factors of a number: ")
for i in range (1, n+1):
    if n%i==0:
        print(i)