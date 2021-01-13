#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # one time pass, 10 min
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if m == 1 or n == 1:
            s = sum([sum(row) for row in obstacleGrid])
            return 0 if s > 0 else 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == m-1 and j == n-1:
                    dp[i][j] = 1
                elif i == m-1:
                    dp[i][j] = dp[i][j+1]
                elif j == n-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
# @lc code=end

