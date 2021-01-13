#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # NO 1 math, O(N), O(N)
        if len(nums)==1:
            return nums[0]
        return (3*sum(set(nums)) - sum(nums)) / 2
        # no 2 bit manipulation, idea i cant explain, O(N), O(1)
        ones, twos = 0, 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & (~twos)
            twos = (twos ^ nums[i]) & (~ones)
        return ones

        # NO 3 hashmap, O(N), O(N)

        # NO 4 sorting, O(NlogN), O(1)
        





# @lc code=end

