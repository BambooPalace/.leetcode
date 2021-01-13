#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # own code, binary search
        if not x or x == 1:
            return x
        left = 0
        right = x
        while left < (right - 1): # but right - 1 took more time in main loop
            mid = (left + right) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                right = mid
            else:
                left = mid
        return left # if left = right - 1, then mid is left

        # # xiaohao, careful about boundary and mid
        # while left < right:
        #     mid = (left + right) / 2 + 1
        #     if mid ** 2 == x:
        #         return mid
        #     elif mid ** 2 > x:
        #         right = mid - 1
        #     else:
        #         left = mid
        # return left
        
# @lc code=end

