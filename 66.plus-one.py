#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # NO 1, done it before, only remember vague idea and still make mistakes...  
        # spent 15min, longer than should have           
        carry = 1
        n = len(digits)
        # res = []
        for i in range(n-1, -1, -1):
            sum_ = digits[i] + carry            
            if sum_ == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = sum_
                carry = 0
            
        if carry == 1:
            digits.append(1)
            digits[0], digits[-1] = digits[-1], digits[0]
        return digits

        # NO 2, many learnt from halfrost
        # 1. no need seperate last digits and others, no need new space, can modify input list

        
# @lc code=end

