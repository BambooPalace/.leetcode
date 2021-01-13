#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # own 20min, fail, not maxint32=2**31-1, minint32=-2**32
        # read instructions! assume that your function returns 231 − 1 when the division result overflows.
        if dividend == 0:
            return 0
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        # bug 1: special for -2147483648 overflows to 2147483647        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  
        dividend = abs(dividend)
        divisor = abs(divisor)
        # optional but faster          
        if divisor == 1:
            return dividend*sign     
        l = 1
        r = dividend
        while l <= r:
            mid = (l + r) // 2
            # does below multiplication break the rule?
            if mid*divisor == dividend:
                return mid*sign
            elif mid*divisor > dividend:
                r = mid-1
            else:                
                l = mid + 1
        return r*sign        

        # NO2 halfrost, to check the solution with bit shifting...







# @lc code=end

