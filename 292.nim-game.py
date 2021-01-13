#
# @lc app=leetcode id=292 lang=python
#
# [292] Nim Game
#

# @lc code=start
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # xiaohao: brainteaser
        # if n % 4 then u must lose
        return n % 4
        
# @lc code=end

