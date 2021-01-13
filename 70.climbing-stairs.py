#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # no 1 recursion exceed time limit...
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # no2 iterative, space O(N)
        # dp = {}
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # no3 iterative, O(1)
        if n == 1:
            return 1
        
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second
# @lc code=end

