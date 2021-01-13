#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # no 1 own code: 35min, stuck...bad idea
        # spent too much time on my own should have check out the solution
        # n = len(matrix)
        # if n != 1:
        #     for i in range(n):
        #         # temp copy of the row to be replaced   
        #         # STUCK 10min++ on how to save last row info             
        #         temp = matrix[i][:]                
        #         for j in range(n):
        #             matrix[n-i-1][j] = matrix[i][j]
        #             if i > 0 and j >= n-i:
        #                 matrix[n-i-1][j] = arc[j]
        

        # no 2 xiaohao rotate layer by layer, harder code and slower
        # temp = 0
        # n = len(matrix)
        # x, y = 0, n-1        
        # while x < y:
        #     s, e = x, y
        #     while s < y:
        #         temp = matrix[x][s]
        #         matrix[x][s] = matrix[e][x]
        #         matrix[e][x] = matrix[y][e]
        #         matrix[y][e] = matrix[s][y]
        #         matrix[s][y] = temp
        #         s += 1
        #         e -= 1
        #     x += 1
        #     y -= 1

        # no 3 halfrost, rotate = vertical flip + transpose, easier to code, fast        
        n = len(matrix)
        i, j = 0, n - 1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        


                
                
                

# @lc code=end

