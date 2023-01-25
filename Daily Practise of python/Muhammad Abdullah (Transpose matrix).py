# a program for finding the transpose of a matrix

# taking no of rows and columns as input
p = int(input("Enter no of rows of a matrix: "))
q = int(input("Enter no of columns of a matrix: "))



# printing the matrix you entered as input
print("Enter the elements of your matrix ")
matrix = [[int(input()) for i in range(q)] for j in range(p)]

print("Your matrix is: ")
for i in range(p):
    for j in range(q):
        print(format(matrix[i][j] , "<4") , end="")
    print()


# creating a transpose matrix  
transpose = [[0 for i in range(p)] for j in range(q)]
for i in range(q):
    for j in range(p):
        transpose[i][j] = matrix[j][i]


# for the transpose of matrix
print("The transpose of your matrix is: ")
for i in range(q):
    for j in range(p):
        print(format(transpose[i][j] , "<4") , end="")
    print()