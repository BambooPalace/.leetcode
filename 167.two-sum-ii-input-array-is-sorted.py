#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # own, 5mins, two pointers
        n = len(numbers)
        l = 0
        r = n - 1
        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ == target:
                return [l+1, r+1]
            elif sum_ < target:
                l += 1
            else:
                r -= 1
        

        
# @lc code=end

