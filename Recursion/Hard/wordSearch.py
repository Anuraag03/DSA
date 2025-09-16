
def wordSearch(board, word):
    dx = [0,-1,0,+1]
    dy = [-1,0,+1,0]
    m = len(board)
    n = len(board[0])
    def dfs(row,col,index):
        if index == len(word):
            return True
        if row<0 or col<0 or row>=m or col>=n or board[row][col]!=word[index]:
            return False
        temp = board[row][col]
        board[row][col] = '#'
        found = dfs(row,col-1,index+1) or dfs(row-1,col,index+1) or dfs(row,col+1,index+1) or dfs(row+1,col,index+1)
        board[row][col] = temp
        return found
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(i,j,0):
                    return True
    return False
                
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "ABCB"
print(wordSearch(board,word))
print(wordSearch(board2,word2))