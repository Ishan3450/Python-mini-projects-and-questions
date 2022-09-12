def matrix(m,n):
    l = []
    for i in range(m):
        row = []
        for j in range(n):
            num = int(input(f"Enter Value of {i} of {j} Position : "))
            row.append(num)
        l.append(row)
    return l

def printMatrix(matrixName):
    for i in matrixName:
        print(i)

def addMatrix(m,n):
    sum = []
    for i in range(len(m)): # Number of Rows
        for j in range(len(A[0])): # Number of Columns
            sum.append(m[i][j]+n[i][j])
    return sum

if __name__ == "__main__":
    m = int(input("Enter Value of m : "))
    n = int(input("Enter Value of n : "))

    print("Enter Matrix A : ")
    A = matrix(m, n)

    print("\nEnter Matrix B : ")
    B = matrix(m, n)

    print("Matrix A :")
    printMatrix(A)
    print("Matrix B :")
    printMatrix(B)

    print("\nSum of Both matirx : ")
    sum = addMatrix(A, B)

    printMatrix(sum)