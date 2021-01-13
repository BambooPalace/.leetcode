#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """        
        # easy adaption based on 54.
        if n == 1:
            return [[1]]
 
        res = [[0] * n for i in range(n)]
        hor = 1
        ver = 0
        i = j = 0              
        dep = 0         
         
        for num in range(1, n*n + 1): 
            res[i][j] = num          
            if i == dep and j == n-1-dep:
                hor = 0
                ver = 1                
            elif i == j == n-1-dep:
                hor = -1
                ver = 0                                         
            elif i == n-1-dep and j == dep:
                hor = 0
                ver = -1     
            elif i == dep + 1 and j == dep:
                hor = 1
                ver = 0
                dep += 1                      
                                                                             
            i += ver
            j += hor      
                                                                    
        return res
        
# @lc code=end

