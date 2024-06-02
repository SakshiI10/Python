# Using list, sum of matrix elements.

n=int(input("Enter size of matrix: "))
if n==0:
    exit()
else:
    mat=[]
    sum=0
    for i in range(0,n):
        ele=int(input("Enter element: "))
        mat.insert(i, ele)
        sum+=mat[i]
    print("\nMatrix is: ")
    for i in range(0, n):
        print(mat[i], end=" ")
    print()
    print("Sum of matrix elements = ",sum)