#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # NO 1, xiaohao logic my own code, dp, space & time O(N^2), 
        # n = len(triangle)
        # # dp[i][j] is the min path passing the element[i][j]
        # path = [[0 for r in row] for row in triangle]
        # path[0][0] = triangle[0][0]        

        # for i in range(1, n):
        #     # for middle elements
        #     for j in range(1, i):
        #         # state transfer function
        #         path[i][j] = min(path[i-1][j-1], path[i-1][j]) + triangle[i][j]
        #     # left most element
        #     path[i][0] = path[i-1][0] + triangle[i][0]
        #     # right most element j = i
        #     path[i][i] = path[i-1][i-1] + triangle[i][i]
        # return min(path[n-1])

        # NO 2, reduce space to O(N), result wrong...debug next time
        n = len(triangle)
        last = [triangle[0][0]]
        cur = []
        for i in range(1, n):
            cur = []
            # left most element
            cur.append(last[0] + triangle[0][0])
            # for middle elements
            for j in range(1, i):
                # state transfer function
                cur.append(min(last[j-1], last[j]) + triangle[i][j])            
            # right most element j = i
            cur.append(last[i-1] + triangle[i][i])
            last = cur

        return min(cur)
        

        
# @lc code=end

