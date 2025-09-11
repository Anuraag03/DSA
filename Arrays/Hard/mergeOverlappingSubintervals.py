def mergeIntervals(intervals):
    intervals.sort()
    res = []
    res.append(intervals[0])
    for i in range(1,len(intervals)):
        if res[-1][1]<intervals[i][0]:
            res.append(intervals[i])
        else:
            res[-1][1] = max(res[-1][1],intervals[i][1])
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))
