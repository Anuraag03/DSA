def stockBuySell(nums):
    buy = nums[0]
    profit = 0
    for i in range(1,len(nums)):
        buy = min(buy,nums[i])
        profit = max(profit,nums[i]-buy)
    return profit

print(stockBuySell([7,1,5,3,6,4]))