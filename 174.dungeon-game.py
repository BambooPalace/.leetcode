#
# @lc app=leetcode id=174 lang=python
#
# [174] Dungeon Game
#

# @lc code=start
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # try dp for 27min, self fix +10min, still FAIL...
        # can't solve HARD on my own so far
        # m = len(dungeon)
        # n = len(dungeon[0])       
        # dp = [[0] * n for _ in range(m)]
        
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #             if i == m-1 and j == n-1:                        
        #                 dp[i][j] = 1
        #             elif j == n-1:
        #                 dp[i][j] = 1 - dp[i+1][j] if dp[i+1][j] < 0 else 1
        #             elif i == m-1:
        #                 dp[i][j] = 1 - dp[i][j+1] if dp[i][j+1] < 0 else 1
        #             else:
        #                 temp = max(dp[i+1][j], dp[i][j+1])
        #                 dp[i][j] = 1 - temp if temp < 0 else 1
        #             dp[i][j] = 1 - dungeon[i][j] if dungeon[i][j] < 0 else 1
        # return dp[0][0]

        # t0 check halfrost... bit tired
        m = len(dungeon)
        n = len(dungeon[0])  
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = max(1-dungeon[m-1][n-1], 1)
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = min(max(1, dp[i][j+1] - dungeon[i][j]), max(1, dp[i+1][j] - dungeon[i][j]))
        return dp[0][0]


        
        
# @lc code=end

