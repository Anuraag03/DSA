def pascalsTriangle(num):
    triangle = []
    for i in range(num):
        row = [1]*(i+1)
        for j in range(1,i):
            row[j] = triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
    return triangle

print(pascalsTriangle(4))