#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # own, 20min cant finish code
        # not difficult, write code out, not brewing in head only
        n = len(nums)
        if nums[0] == target:
            return 0
        if n == 1 and nums[0] != target:
            return -1
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                # stuck from here, continue based on GARVIT
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # stuck thinking in head, just try to write code out will be clear
            else:
                if target < nums[mid] or target >= nums[l]:                    
                    r = mid - 1
                else:
                    l = mid + 1
        return -1






        
# @lc code=end

