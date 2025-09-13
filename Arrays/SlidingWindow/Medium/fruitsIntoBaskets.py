'''
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. 
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) 
while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
'''

def fruitsInBasket(fruits):
    bucket1 = -1
    bucket2 = -1
    bucket1Count = 0
    maxFruits = 0
    currCount = 0
    for i in fruits:
        if i==bucket1 or i==bucket2:
            currCount+=1
        else:
            currCount = bucket1Count+1
        if i == bucket1:
            bucket1Count+=1
        else:
            bucket1Count = 1
            bucket2,bucket1 = bucket1,i
        maxFruits = max(maxFruits,currCount)
    return maxFruits

print(fruitsInBasket([1,2,3,2,2]))

