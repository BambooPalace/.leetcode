#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no 1: dp on my own yay!, think about sol for 14min; code for 2(forget edge cases) + 5min
        # beat % not stable ... nvm, O(N) & O(N), dp prob space can always optimize
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)                
        dp = {}
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]

        
# @lc code=end

