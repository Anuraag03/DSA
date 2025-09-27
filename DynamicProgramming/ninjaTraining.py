'''
A Ninja has an N Day training schedule. 
He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. 
There are merit points associated with performing an activity each day. 
The same activity can't be performed on two consecutive days. 
We need to find the maximum merit points the ninja can attain in N Days.
We are given a 2D Array POINTS of size N*3 which tells us the merit point of 
specific activity on that particular day. 
Our task is to calculate the maximum number of merit points that the ninja can earn.
'''
def ninjaTrainingM(n,points): #TC: O(N*3*3) SC:O(N*3)
    m = len(points[0])
    dp = [[-1]*(m) for _ in range(n)]
    def rec(day,last):
        if day == 0:
            maxi = float('-inf')
            for i in range(3):
                if last!=i:
                    maxi = max(maxi,points[day][i])
            return maxi

        if dp[day][last]!=-1:
            return dp[day][last]
        maxTotal = 0
        for i in range(m):
            
            if last != i:
                total = rec(day-1,i)+points[day][i]
                maxTotal = max(maxTotal,total)
        dp[day][last] = maxTotal
        return dp[day][last]
    return rec(n-1,-1)

def ninjaTrainingT(n,points):#TC = O(N*3*4) SC:O(N*3)
    m = len(points[0])
    dp = [[0]*(m+1) for _ in range(n)]
    dp[0][0] = max(points[0][1],points[0][2])
    dp[0][1] = max(points[0][1],points[0][2])
    dp[0][2] = max(points[0][1],points[0][2])
    dp[0][3] = max(points[0][0],points[0][1],points[0][2])
    for day in range(1,n):
        for last in range(m+1):
            dp[day][last] = 0
            for k in range(m):
                if k!=last:
                    total = points[day][k]+dp[day-1][k]
                    dp[day][last] = max(dp[day][last],total)
    return dp[n-1][m]



points = [[10,40,70],[20,50,80],[30,60,90]]
print(ninjaTrainingM(len(points),points))
print(ninjaTrainingT(len(points),points))
