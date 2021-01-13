#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dont understand question, isnt max the peak?, check solution directly
        # NO1 official 1, I SEE, only need to find ANY ONE peak...
        # for i in range(len(nums)-1):
        #     if nums[i] > nums[i+1]:
        #         return i
        # return len(nums) - 1

        # NO2 own, WRONG, i dont understand my sol either...
        # n = len(nums)
        # if n == 1:
        #     return 0
        # l = 0
        # r = n - 2
        # while l <= r:
        #     mid = (l+r) // 2
        #     if nums[mid] > nums[mid+1]:
        #         return mid
        #     else: # bug 2: wrong section to continue
        #         # r = mid - 1
        #         l = mid + 1
        # # bug1: fail [1,2], ??? i thought last element always smaller
        # return n - 1

        # NO2 official 3, and Garvit, dont understand well
        left, right = 0, len(nums)-1
        while left < right:
        	mid = (left + right) /2
        	if nums[mid] > nums[mid+1]:
        		right = mid
        	else:
        		left = mid + 1
        return left


    




# @lc code=end

