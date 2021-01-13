#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) <= 3:
            return max(nums)
        n = len(nums)
        # simple trick but tricky to think of haha
        res = max(self.helper(nums[:n-1]), self.helper(nums[1:]))
        return res

    def helper(self, arr):
        dp = {}
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            dp[i] = max(dp[i-1], dp[i-2]+arr[i])
        return dp[len(arr)-1]

        
# @lc code=end

