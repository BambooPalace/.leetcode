#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # try own, 9 min, onetime PASS
        # path problem seem easy to me
        dp = [[0] * n for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                elif i == m-1:
                    dp[i][j] = dp[i][j+1]
                elif j == n-1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

        # check xiaohao, opportunity for optimization




# @lc code=end

