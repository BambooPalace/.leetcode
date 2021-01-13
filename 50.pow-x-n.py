#
# @lc app=leetcode id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # no idea, straight to halfrost; dont see much sense in this problem...
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1 / x
        
        temp = self.myPow(x, n/2)
        if n%2 == 0:
            return temp * temp
        return temp * temp * x
        
# @lc code=end

