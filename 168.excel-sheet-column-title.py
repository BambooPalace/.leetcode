#
# @lc app=leetcode id=168 lang=python
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # not difficult, but tricky
        # NO 1 leetcode discuss & halfrost
        res = ''
        while n:
            # learned switch char and num
            res = chr(ord('A') + (n-1)%26) + res
            n = (n-1)//26
        return res


        
# @lc code=end

