def solveSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empties = []
    # Initialize sets
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                empties.append((r, c))
            else:
                val = board[r][c]
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r//3)*3 + (c//3)].add(val)
    def backtrack(i=0):
        if i == len(empties):
            return True  # all filled
        r, c = empties[i]
        b = (r//3)*3 + (c//3)
        for ch in "123456789":
            if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                # place digit
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)
                if backtrack(i+1):
                    return True
                # undo move (backtrack)
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)
        return False
    backtrack()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
print(board)