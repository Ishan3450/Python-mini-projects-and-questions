# this is the first time i used the import statement to import functions of the file
import addingTwoMatrics

m = int(input("Enter Value of m :"))
n = int(input("Enter Value of n :"))

l = [] # this list is to store multiplication of both matrix

print("Enter Matrix A : ")
a = addingTwoMatrics.matrix(m, n)
addingTwoMatrics.printMatrix(a)

print("Enter Matrix B : ")
b = addingTwoMatrics.matrix(m, n)
addingTwoMatrics.printMatrix(b)

for i in range(m):
    for j in range(n):
        row = []
        num = a[i][j] * b[j][i]
        row.append(num)
    l.append(row)

print("Multiplication of Both Matrix is : ")
addingTwoMatrics.printMatrix(l)