#
# @lc app=leetcode id=343 lang=python
#
# [343] Integer Break
#

# @lc code=start
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        #SPENT 1 hr
        # own thought and code, 30 min, ver 1 wrong + some mod from xiaohao
        dp = {}       
        dp[2] = 1
        dp[3] = 2
        # as dp[n] >= n for n>=4
        # if n < 4:
        #     return dp[n]
        # for i in range(4, n+1):
        #     if i >= 8:
        #         # ver1 my own idea wrong: dp[i] = dp[i//2]*dp[i - i//2]
        #         dp[i] = 0
        #         # coz i know dp[i] > dp[i-1], where j = 1
        #         for j in range(2, i//2 + 1):
        #             # iterates to find max by greedy method                    
        #                 dp[i] = max(dp[i], max(dp[j], j) * dp[i - j])                    
        #     else:
        #         dp[i] = (i//2) * (i - i//2)
        # return dp[n]

        # no 2 based on xiaohao
        for i in range(4, n+1):
            dp[i] = 0
            # dp[i] > dp[i-1], thus skip j=1
            for j in range(2, i//2+1):
                dp[i] = max(dp[i], max(dp[j], j) * max(dp[i-j], (i-j)))
        return dp[n]
        # no 3 xiaohao
        # dp[1] = 1
        # while i < n and j < i:
        # dp[i] = max(dp[i], max(dp[j], j) * (i - j))

        
# @lc code=end

