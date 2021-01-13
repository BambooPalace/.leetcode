#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # NO1, try modify based on I, no idea after 5mins, check GARVIT
        n = len(nums)
        if nums[0] == target:
            return True
        if n == 1 and nums[0] != target:
            return False
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:                
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if target < nums[mid] or target >= nums[l]:                    
                    r = mid - 1
                else:
                    l = mid + 1
            # Garvit only add this line
            else: # nums[mid] == nums[l]
                l += 1
        return False
        
# @lc code=end

