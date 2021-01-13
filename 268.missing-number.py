#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no 1 math, sum(1 to n) = n*(n+1)/2, O(N), O(1)
        n = len(nums)
        # return n*(n+1)/2 - sum(nums)

        # NO 2 bit manipulation
        res = 0
        for i in range(n):
            res ^= nums[i] ^ i
        return res ^ n

        
# @lc code=end

