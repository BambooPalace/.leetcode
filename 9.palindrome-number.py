#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        elif x < 0 or x%10 == 0:
            return False
        
        res = 0

        # below condition cant cover multiple of 10
        while res < x:
            # below 2 lines wrong
            # if res != x:
            #     return False
            res = res*10 + (x%10)
            x = x / 10
        if res == x or res/10 == x:
            return True


        
# @lc code=end

