#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no 1 own, hash map, O(2N), O(N)
        # code can be cleaner tho
        # if len(nums) == 1:
        #     return nums[0]
        # h = {}
        # for c in nums:
        #     if c in h:
        #         h[c] -= 1
        #     else:
        #         h[c] = 1
        # for k, v in h.items():
        #     if v > 0:
        #         return k

        # no 2 xiaohao, XOR operator, O(N), O(1)
        # a^b = 0 if a==b else 1; a^0 = a； a^a = 0
        #
        res = 0
        for num in nums:
            res ^= num
        return res
        
        # no 3, official, set and math
        # set takes O(N) space, sum takes O(N) time
        # return 2*sum(set(nums)) - sum(nums)


        
# @lc code=end

