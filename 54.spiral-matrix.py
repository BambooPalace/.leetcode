#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]        
        """
        # SPENT 80mins in total, try to use my own code, unsuccessful debug
        # NO 1 own idea and code 30min, debug on stop condition 10 min

        # while i < m and i >= m0 and j < n and j >= n0: # my idea on stop condition
        # while m0 <= m and n0 <= n: # xiaohao idea, easier to understand                
            
                
        # NO 2 modify code, if code boundary unclear, introduce better variables        
        m = len(matrix)
        n = len(matrix[0]) # return type is list
        if m == 1:
            return matrix[0]
        if n == 1:
            return [r[0] for r in matrix]
        res = []
        hor = 1
        ver = 0
        i = j = 0
        count, total = 0, m*n      
        left, right, up, down = 0, n-1, 0, m-1          
        # while left <= right and up <= down:   
        while count < total: # more helpful incase boundary condition hard to write  
            res.append(matrix[i][j])
            # wrong for case [[1,2,3,4],[5,6,7,8],[9,10,11,12]], 
            # when 4 corners collapse to 2 corners, so add below two conditions
            if up == down:
                hor = 1
                ver = 0
            elif left == right:
                hor = 0
                ver = 1 
            elif i == up and j == right:
                hor = 0
                ver = 1                
            elif i == down and j == right:
                hor = -1
                ver = 0                                         
            elif i == down and j == left:
                hor = 0
                ver = -1  
            elif i == up + 1 and j == left:
                hor = 1
                ver = 0
# only up finish one loop can update boundary, otherwise above conditions will be messed up
                up += 1  
                right -= 1    
                down -= 1  
                left += 1                            
                                                                             
            i += ver
            j += hor      
            count += 1                                                          
        return res

        # # no 3 halfrost
        # count, total = 0, m*n
        # while count < total:
        #     i, j = up, left
        #     # and count < total: this innner condition works for some confused reason:
        #     # otherwise this case will fail [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        #     while j <= right:# and count < total:
        #         res.append(matrix[i][j])
        #         j += 1
        #         count += 1
            
        #     i, j = up+1, right
        #     while i <= down:# and count < total:
        #         res.append(matrix[i][j])
        #         i += 1
        #         count += 1
            
        #     i, j = down, right-1
        #     while j >= left:# and count < total:
        #         res.append(matrix[i][j])
        #         j -= 1
        #         count += 1

        #     i,j = down-1, left
        #     while i > up:# and count < total:
        #         res.append(matrix[i][j])
        #         i -= 1
        #         count += 1
        #     up += 1
        #     down -= 1
        #     left += 1
        #     right -= 1
        # return res






        
    
# @lc code=end

