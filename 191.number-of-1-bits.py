#
# @lc app=leetcode id=191 lang=python
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # no 1 own math wrong
        # 00000000000000000000000000001011 is 11 hemming/bit wise num, not 1011
        # res = 0
        # while n > 0:
        #     res += (n % 10)
        #     n = n // 10
        # return res

        # no 2 halfrost, X = X & ( X -1 ) 这个操作可以清除最低位的二进制位 1
        # res = 0
        # while n > 0:
        #     n = n & (n-1)
        #     res += 1
        # return res

        # no 3 xiaohao, bit mask
        res = 0
        mask = 1 #000...0001
        for i in range(32):
            if n&mask != 0:
                res += 1
            mask = mask << 1
        return res


        



        
# @lc code=end

