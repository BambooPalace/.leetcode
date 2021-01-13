#
# @lc app=leetcode id=190 lang=python
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # confusing...
        # NO1 halfrost, 
        res = 0
        for i in range(32):
            # rigt most bit is n&1
            # combine operation can be either + or |
            res = res<<1 | n&1
            # iterate bit from right to left
            n >>= 1
        return res
        # NO2 official
        # ret, power = 0, 31
        # while n:
        #     ret += (n & 1) << power
        #     n = n >> 1
        #     power -= 1
        # return ret

        # # NO3 Garvit
        # res = 0
        # for i in range(32):
        #     res += n & 1
        #     n = n >> 1
        #     if i != 31:
        #         res = res << 1
        # return res
        
# @lc code=end

