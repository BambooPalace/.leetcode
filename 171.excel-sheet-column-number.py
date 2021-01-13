#
# @lc app=leetcode id=171 lang=python
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # simple but hard to think of on my own, should get more familiar
        val, res = 0, 0
        for c in s:
            val = ord(c) - ord('A') + 1
            res = res*26 + val
        return res




        
# @lc code=end

