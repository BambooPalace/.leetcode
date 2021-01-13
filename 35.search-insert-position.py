#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # NO 1 own, 10 min code, 10 min debug and modify
        n = len(nums)
        # bug2: [1], 1; satisfy both of below, treat as 1st case as required
        # bug3: below edge case handling is bad, should have tested a few
        # if target <= nums[0]:
        #     return 0
        # if target > nums[-1]:
        #     return n # bug1: n - 1, note the exampels...
        # # below line is optional, normal code can also get
        # if target == nums[-1]: 
        #     return n - 1

        # NO 2 modified version, above edge case is not necessary, below can handle all
        
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo if nums[lo] >= target  else lo + 1# hi = lo here

        

        
# @lc code=end

