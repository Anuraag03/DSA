def spiralMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    i = 0
    j = -1
    direction = 1
    res = []
    while row>=0 and col>=0:
        if direction:
            for _ in range(col):
                j+=1
                res.append(matrix[i][j])
            row-=1
            for _ in range(row):
                i+=1
                res.append(matrix[i][j])
            col-=1
            direction-=1
        else:
            for _ in range(col):
                j-=1
                res.append(matrix[i][j])
            row-=1
            for _ in range(row):
                i-=1
                res.append(matrix[i][j])
            col-=1
            direction+=1
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))
            

