#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # no1 own code only 10 min!   debug 10 mins     
        m = len(matrix)
        n = len(matrix[0])
        if m == n == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        lo = 1
        hi = m * n
        r = c = 0
        while lo <= hi:
            mid = (lo + hi) //2
            # idea: just convert num to row and cols, can make a helper function
            if mid % n == 0:
                r = mid // n -1
                c = n - 1
            else:
                r = mid // n
                c = mid % n - 1
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                lo = mid + 1
            else:
                # bug reason: wrote hi = mid; 
                # confused: is below line universial for binary search problems
                hi = mid - 1
        return False
        # DEBUG: [1,3], 1; output wrong, modify based on xiaohao



        
# @lc code=end

