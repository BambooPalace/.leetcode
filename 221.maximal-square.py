#
# @lc app=leetcode id=221 lang=python
#
# [221] Maximal Square
#

# @lc code=start
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # own, 5min NO idea
        # def findOnes(row):
        #     '''
        #     :type row: List[int]
        #     :rtype: int
        #     '''
        #     maxlength = 0
        #     for i in range(len(row)):
        #         if i == 0:
        
        # NO2 official solution


        # NO3 NEETCODE, DP(bottom up) & recursive(top down), 
        m = len(matrix)
        n = len(matrix[0])
        cache = {}
        #cache[(i,j)], alternative to cache[i][j]

        def helper(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) not in cache:
                down = helper(i+1, j)
                right = helper(i, j+1)
                diag = helper(i+1, j+1)

                cache[(i,j)] = 0
                if matrix[i][j] == '1':
                    cache[(i,j)] = 1 + min(down, right, diag)
            return cache[(i,j)]
        helper(0,0)
        return max(cache.values()) ** 2





                



        
# @lc code=end

