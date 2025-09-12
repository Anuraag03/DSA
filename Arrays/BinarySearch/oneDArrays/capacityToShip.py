class Solution:
    def shipWithinDays(self,weights,days):
        arrSum = sum(weights)
        maxCapacity = arrSum
        ans = maxCapacity
        def canShip(capacity):
            day = 1
            shipmentLoad = 0
            for i in weights:
                if shipmentLoad+i<=capacity:
                    shipmentLoad+=i
                else:
                    day+=1
                    shipmentLoad = i
           
            return day==days
            


        for i in range(maxCapacity,0,-1):
            if canShip(i): 
                ans = i
        return ans

s = Solution()
print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))