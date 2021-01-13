#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max 1 transaction
        # NO 1, done this before, can't remember how to do...
        # below NOT work...
        # n = len(prices)
        # buy = 0
        # sell = n-1
        # for i in range(n):
        #     if prices[i] > prices[sell]:
        #         sell = i
        #     elif prices[i] < prices[buy]:
        #         buy = i
        # if sell > buy:
        #     return prices[sell] - prices[buy]
        # else:
        #     return 0

        # no2 official sol
        minprice = float('inf')
        res = 0
        
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice) > res:
                res = prices[i] - minprice
        return res

        
        


# @lc code=end

