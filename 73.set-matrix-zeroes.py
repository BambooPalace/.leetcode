#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # try own 10min, find idices of 0, then update, O(mxn), O(m+n)
        m = len(matrix)
        n = len(matrix[0])
        rows = []
        cols = []
        # search idx
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:    
                    # can be replaced as set.add()                
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        # [ver 1]update idx, 104ms. This is faster?  m + n
        for row in rows:
            matrix[row] = [0] * n
        for i in range(m):
            for col in cols:
                matrix[i][col] = 0
        
        #[ver 2] from official sol, 116ms, mxn SLOWER
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        # NO2 space O(1)? neetcode, check in future, not feel like it
        
        
# @lc code=end

