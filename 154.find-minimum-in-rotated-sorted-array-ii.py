#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # xiaohao
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0 
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            # special handling
            else:
                right -= 1
                # left += 1 # line from halfrost, wrong for [10,1,10,10,10]
        return nums[left]
        
# @lc code=end

