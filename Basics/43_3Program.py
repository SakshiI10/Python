# Using List, find smallest and largest element in matrix.

n=int(input("Enter size of matrix: "))
matrix=[]
sum=0
for i in range(0, n):
    ele=int(input("Enter element: "))
    matrix.insert(i, ele)
print("\nArray is: ")
for i in range(0, n):
    print(matrix[i], end='')
print()
largest=max(matrix)
l_index=matrix.index(largest)
smallest=min(matrix)
s_index=matrix.index(smallest)
print("Largest element is ", largest, "at position", l_index+1)
print("Smallest element is ", smallest, "at position", s_index+1)