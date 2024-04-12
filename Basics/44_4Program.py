# Using list, create 2D matrix.

r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
matrix = []

#print("Elements in row wise manner: ")

for i in range(r):
    a=[]
    print("Enter",c,"elements of row",i+1,": ")
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
    
print("Entered matrix is: ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()
    