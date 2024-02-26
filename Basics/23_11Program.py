# Print Prime numbers in 1 to 100

n=("Prime numbers between 1 to 100 are: ")
for n in range(1, 101):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n, end=" ")