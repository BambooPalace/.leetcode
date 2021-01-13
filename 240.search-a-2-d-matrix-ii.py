#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # NO1 own 8 min, one time PASS! worse O(m*nlogn)
        # i am good binary search ard
        m = len(matrix)
        n = len(matrix[0])                
        # def searchRow(row):
        #     l = 0
        #     r = n - 1
        #     if target < row[0] or target > row[-1]:
        #         return False
        #     while l <= r:
        #         mid = (l+r) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return False
        
        # for i in range(m):
        #     if searchRow(matrix[i]):
        #         return True
        # return False   

        # NO2 halfrost, GOOD idea! O(m+n)
        row = 0
        col = n - 1
        while col >= 0 and row <= m-1:
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False
 

        
# @lc code=end

