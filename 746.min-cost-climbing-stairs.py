#
# @lc app=leetcode id=746 lang=python
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # own, dp[i]: min cost to reach idx i, 1st code 8min
        # bug1: can start either at 0 or 1, 5min
        # dp = {}
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, len(cost)+1):
        #     dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        # return dp[len(cost)] - cost[-1]
        # bug 2: FAIL [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        # my logic is wrong... dont get the questions very well

        # NO2, leetcode discuss, dp[i] is cost to stand on ith start including cost[i], 
        # cost[i] means cost to climb from ith stair, discuss abt res is to stand on 
        n = len(cost)
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2]) # bit confusing also



        
# @lc code=end

