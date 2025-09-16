def generateParanthesis(num):
    res = []
    def rec(str,open,close):
        if len(str) == 2*num:
            res.append(str)
            return
        if open<num:
            rec(str+'(',open+1,close)
        if close<open:
            rec(str+')',open,close+1)
    rec('',0,0)
    return res

print(generateParanthesis(3))
