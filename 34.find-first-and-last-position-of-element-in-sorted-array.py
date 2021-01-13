#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # NO1 based on halfrost, seperate task of finding 1st and last
        if not nums:
            return [-1, -1]
        n = len(nums)
        if n == 1 and nums[0] == target:
            return [0, 0]
        if n == 1 and nums[0] != target:
            return [-1, -1]
        
        l = 0
        r = n - 1
        res = []
        # find 1st element
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    res.append(mid)
                    break
                else:
                    r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if not res:
            return [-1, -1]
        
        # find last element
        l = res[0]
        r = n - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                if mid == n-1 or nums[mid+1] != target:
                    res.append(mid)
                    break
                else:
                    l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if len(res) == 1:
            res.append(res[0])
        return res
        
        # NO2 to check official(same as Garvit), key is use one function to get either leftmost or rightmost index
        # returns leftmost (or rightmost) index at which `target` should be inserted in sorted array `nums` via binary search.
        def extreme_insertion_index(self, nums, target, left):
            lo = 0
            hi = len(nums)

            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid+1

            return lo


        
# @lc code=end

