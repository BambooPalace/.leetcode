#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # basically sorting, no idea, straight to solution
        # NO1 halfrost, count and sort, O(N), O(K) k=3 here
        # CANT understand CODE... shouldnt spent time reading
       
        
        # own, brute, two pass, 24ms
        # if len(nums) <= 1:
        #     return nums
        # counter = {}
        # counter[0] = 0
        # counter[1] = 0
        # counter[2] = 0
        # for num in nums:
        #     if num == 0:
        #         counter[0] += 1
        #     elif num == 1:
        #         counter[1] += 1
        #     elif num == 2:
        #         counter[2] += 1
        # i = 0
        # while counter[0] > 0:
        #     counter[0] -= 1
        #     nums[i] = 0
        #     i += 1
        # while counter[1] > 0:
        #     counter[1] -= 1
        #     nums[i] = 1
        #     i += 1
        # while counter[2] > 0:
        #     counter[2] -= 1
        #     nums[i] = 2
        #     i += 1
        
        # Garvit, CANT understand after coding, should have watched video explanation
        # 24ms, understand from TECHDOSE
        if len(nums) <= 1:
            return nums
        start, end = 0, len(nums) - 1
        i = 0 # middle pointer
        while i <= end:
            if nums[i] == 1: # middle number keep
                i += 1
            elif nums[i] == 0: # swap with low pointer
                nums[i], nums[start] = nums[start], nums[i]
                i += 1
                start += 1
            else: # swap with end pointer
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
        

        

        
# @lc code=end

