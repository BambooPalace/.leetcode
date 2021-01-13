#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # own intuition: 1 get list of valley and peaks;choose two subsets maximize profits
        # HALT thinking as hard problem

        # no 2 Garvit DP, DONT understand
        n = len(prices)
        if n == 1:
            return 0
        dp = [[0] * n for _ in range(3)]
        for i in range(1,3):
            maxDiff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + maxDiff)
                maxDiff = max(maxDiff, dp[i-1][j] - prices[j])
            return dp[2][n-1]


        
# @lc code=end

