def findRowWithMax1s(matrix): # assuming rows in array are sorted , else sort them first
    def firstOccurance(row):
        l = 0
        r = len(row)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if row[mid]==1:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
    maxNum = 0
    row = -1
    for i in range(len(matrix)):
        pos = firstOccurance(matrix[i])
        if pos!=-1:
            count=len(matrix[0])-pos
        if count>=maxNum:
            maxNum = count
            row = i
    return row,maxNum

matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
print(findRowWithMax1s(matrix))
        






