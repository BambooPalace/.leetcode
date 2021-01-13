#
# @lc app=leetcode id=279 lang=python
#
# [279] Perfect Squares
#

# @lc code=start
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # own, CANT THINK OG
        # if n**0.5 % 1 ==0:
        #     return 1

        # Garvit
        dp = {}
        # squares
        sq = [i*i for i in range(1, int(n**0.5)+1)]
        for s in sq:
            dp[s] = 1
        if n in dp:
            return 1
        for i in range(1, n+1):
            if i not in dp:
                dp[i] = float('inf')
                for s in sq:
                    if s < i:
                        dp[i] = min(dp[i], dp[s] + dp[i-s])
        return dp[n]
        


        
# @lc code=end

