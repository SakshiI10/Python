#Print numbers 1...100. CHange line after each 10 numbers.

for i in range(1, 101):
    print(i, end=" ")
    if (i%10==0):
        print()