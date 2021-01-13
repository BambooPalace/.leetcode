#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # by memory, check valley and peak, bad method
        # many case fail as my code didnt handle last element well
        # n = len(prices)
        # valley = 0
        # peak = 0
        # i = 0
        # res = 0
        
        # while i < n-1:
        #     if prices[i] < prices[i+1] and prices[i] < prices[i-1]:
        #         valley = i
        #     if prices[i] > prices[valley] and prices[i] > prices[i+1]:
        #         peak = i
        #     i += 1            
        #     if peak > valley:                
        #         res += prices[peak] - prices[valley]
        # # check if last one is peak, coz method is method, if condition is hard to write...
        # if peak < valley: # bug1: [6,1,3,2,4,7]
        #     peak = valley
        # if prices[-1] > prices[peak]:
        #     res += prices[-1] - prices[valley]
        # return res

        # no 2: one pass, add section if increasing
        n = len(prices)
        if n == 1:
            return 0
        res = 0
        for i in range(1,n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
        




        
        
# @lc code=end

