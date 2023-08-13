# Print numbers 1...100. Change line after each 10 numbers.

a=1
while a<=100:
    print(a, end=" ")
    if a%10==0:
        print()
    a=a+1