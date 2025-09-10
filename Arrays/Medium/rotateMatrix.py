def rotate90DegreeClockWise(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in matrix:
        i.reverse()

def rotate90DegreeAntiClockWise(matrix):
    n = len(matrix)
    for i in matrix:
        i.reverse()
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
rotate90DegreeClockWise(matrix)
rotate90DegreeAntiClockWise(matrix2)
print(matrix)
print(matrix2)