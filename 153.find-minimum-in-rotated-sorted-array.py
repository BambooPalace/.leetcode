#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # tip: min num is in unsorted side
        # no 1 own code by memory, messy        
        left = 0
        right = len(nums) - 1        
        
        # while left < right:
        #     mid = (left + right) / 2 + 1
        #     if nums[mid] > nums[-1] and nums[mid+1] < nums[-1]:
        #         return nums[mid+1]
        #     elif nums[mid] < nums[-1] and nums[mid+1] < nums[-1]:
        #         right = mid - 1
        #     else:
        #         left = mid
        # return nums[mid]

        # no 2 xiaohao, boundary condition i am confused now
        if nums[0] <= nums[-1]: # include len=0 case
            return nums[0]
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid + 1 # why plus 1
            else:
                right = mid                                
        return nums[left]
        # # no 3 official, logic more complex than other sol...
        # while right >= left:
        #     mid = (left + right) / 2
        #     if nums[mid] > nums[mid + 1]:
        #         return nums[mid + 1]
        #     if nums[mid] < nums[mid - 1]:
        #         return nums[mid]
        #     if nums[mid] > nums[0]:
        #         left = mid + 1
        #         right = mid - 1
            







        
        
# @lc code=end

