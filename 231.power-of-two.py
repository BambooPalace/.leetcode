#
# @lc app=leetcode id=231 lang=python
#
# [231] Power of Two
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # NO 1 self, O(logN)
        # if n <= 0:
        #     return False
        # while n > 2:
        #     if n % 2 > 0:
        #         return False
        #     # ceiling division
        #     n = n/2 + n % 2
        # if n <= 2:
        #     return True

        # NO 2 xiaohao, O(1)
        # bitwise, if n is power of 2 then n&(n-1) is 0
        return n>0 and n&(n-1) == 0

    

# @lc code=end

