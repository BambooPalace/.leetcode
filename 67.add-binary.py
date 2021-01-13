#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # no 1 brute, 9 min draft + 10 min debug
        n = max(len(a), len(b))
        a = int(a)
        b = int(b)
        sum_ = str(a + b)        
        res = ''
        carry = 0
        for i in range(1, n+1):
            
            num = int(sum_[-i]) + carry
            if num >= 2:
                # bug 1: str does not support assignment as list... 10 min modify

                res = str(num - 2) + res
                carry = 1
            else:
                res = str(num) + res
                carry = 0
        if carry == 1:
            res = '1' + res            
        return res

        
# @lc code=end

