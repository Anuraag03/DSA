'''
There are several cards arranged in a row, and each card has an associated number of points. 
The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. 
You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''
def maxPoints(cardPoints,k):
    lSum = 0
    rSum = 0
    l = 0
    r = len(cardPoints)-1
    for l in range(k):
        lSum+=cardPoints[l]
    maxSum = lSum
    while l>=0:
        lSum-=cardPoints[l]
        rSum+=cardPoints[r]
        maxSum = max(lSum+rSum,maxSum)
        l-=1
        r-=1
    return maxSum

cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxPoints(cardPoints,k))

