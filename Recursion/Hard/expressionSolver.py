from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(path, pos, value, prev):
            # Base case: reached end of num
            if pos == len(num):
                if value == target:
                    res.append(path)
                return
            
            # Try all splits
            for i in range(pos, len(num)):
                # Skip numbers with leading zero
                if i > pos and num[pos] == "0":
                    break
                
                curr_str = num[pos:i+1]
                curr = int(curr_str)
                
                if pos == 0:
                    # First number → start expression
                    backtrack(curr_str, i+1, curr, curr)
                else:
                    # Addition
                    backtrack(path + "+" + curr_str, i+1, value + curr, curr)
                    # Subtraction
                    backtrack(path + "-" + curr_str, i+1, value - curr, -curr)
                    # Multiplication
                    backtrack(path + "*" + curr_str, i+1, value - prev + prev*curr, prev*curr)
        
        backtrack("", 0, 0, 0)
        return res
