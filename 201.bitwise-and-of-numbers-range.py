#
# @lc app=leetcode id=201 lang=python
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # brute, memory error for 0 to 2147483647 (overflow)
        if m == n:
            return m&n
        res = m        
        for i in range(m+1, n+1):
            res &= i
        return res

        # halfrost


        
# @lc code=end

