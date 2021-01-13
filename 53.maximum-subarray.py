#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # xiaohao logic + my code; O(N), O(N)
        # dp = {}
        # dp[0] = nums[0]
        # n = len(nums)
        # for i in range(1, n):
        #     if dp[i-1] > 0:
        #         dp[i] = dp[i-1] + nums[i] 
        #     else:
        #         dp[i] = nums[i]
        # return max(dp.values())


        # no 2 modify， space to O(1), clean code
        # res = nums[0]
        # max = res
        # for i in range(1, len(nums)):
        #     if res > 0:
        #         res += nums[i]
        #     else:
        #         res = nums[i]
        #     # # alternative code
        #     # if res < 0:
        #     #     res = 0
        #     # res += nums[i]
        #     if res > max:
        #         max = res
        # return max

        # no 3 Garvit, very clean code
        currSum, result = nums[0], nums[0]

        for index in range(1, len(nums)):
        	currSum = max(nums[index], currSum+nums[index])
        	result = max(result, currSum)

        return result

        
# @lc code=end

