#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        # No 1. similar to 120.triangle, think of the sol on my own! YAY!
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[0] * n] * m
        # dp[0][0] = grid[0][0]
        # for i in range(m):            
        #     for j in range(n):
        #         if i == 0 and j > 0:
        #             dp[i][j] = dp[i][j-1] + grid[i][j]
        #         elif j == 0 and i > 0:
        #             dp[i][j] = dp[i-1][j] + grid[i][j]
        #         elif i > 0 and j > 0:
        #             dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        # return dp[m-1][n-1]

        # No 2. minor improvements to make it run faster, beat 93% and 95%   
        m = len(grid)
        n = len(grid[0])
        if m==1 and n==1:
            return grid[0][0]

        dp = [[0] * n] * m
        dp[0][0] = grid[0][0]
        # special handle row 1: i=0
        for j in range(1, n):                
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):            
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[m-1][n-1]


        
# @lc code=end

