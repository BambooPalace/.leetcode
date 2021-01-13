#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # NO1 own, want to try DP, no can do
        # 
        # dp = {}
        # dp[1] = True
        # dp[2] = nums[0] >= 1
        # for i in range(2, n+1):
        #     dp 
        # return dp[n]

        # NO2, own, if NO 0 and len>1, must be true; 15min + 10min debug      
        # run slow if many 0s in the array, wort is O(N^2)
        # n = len(nums)
        # if n == 1: # bug1: forget edge case
        #     return True
        # res = True
        # for i in range(n):
        #     if nums[i] == 0:
        #         res = False
        #         for j in range(i-1, -1, -1):
        #             # bug2: if last num is 0, nums[j] >= i-j is ok
        #             if i==n-1 and nums[j] >= i-j:
        #                 res = True
        #             elif nums[j] > i-j:
        #                 res = True                    
        #         if not res:
        #             return res
        # return res

        # NO3, halfrost, good idea and simple logic! one pass, O(N)        
        if len(nums) == 1:
            return True
        maxJump = 0 # of last index
        for i, v in enumerate(nums):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i+v)
        return True

        # NO4, official solutions many but explanations BAD
            


        
# @lc code=end

