def trappingRainWater(nums): #TC: O(N) SC:O(1)
    left = 0
    right = len(nums)-1
    leftMax = 0
    rightMax = 0
    water = 0
    while left<right:
        if nums[left]<nums[right]:
            if nums[left]>=leftMax:
                leftMax = nums[left]
            else:
                water+=(leftMax-nums[left])
            left+=1
        else: 
            if nums[right]>=rightMax:
                rightMax = nums[right]
            else:
                water+=(rightMax-nums[right])
            right-=1
    return water

def stackApproach(height): #TC: O(N) SC:O(N)
    stack = []
    water = 0
    n = len(height)

    for i in range(n):
        while stack and height[stack[-1]]<height[i]:
            bottom = height[stack.pop()]
            if not stack:
                break
            left = stack[-1]
            width = i-left-1
            boundedHeight = min(height[left],height[i])-bottom
            water+=width*boundedHeight
        stack.append(i)
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(stackApproach(height))  # 6


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingRainWater(height))