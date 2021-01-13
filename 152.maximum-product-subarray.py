#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp, try own, 4min, false idea
        # n = len(nums)
        # dp = {}
        # dp[1] = nums[0]
        # dp[2] = dp[1] if nums[1] < 1 else dp[1]*nums[1]
        # for i in range(3, n+1):
        #     num = nums[i-1]
        #     dp[i] = dp[i-1] if num < 1 else dp[i-1]*num

        # NO2 halfrost, roughly understand after a video
        n = len(nums)
        min_ = max_ = res = nums[0]
        for i in range(1, n):
            num = nums[i]
            if num < 0:
                max_, min_ = min_, max_
            max_ = max(num, max_*num)
            min_ = min(num, min_*num)
            res = max(res, max_)
        return res

    

        
# @lc code=end

