#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # NO1 hashmap, O(n), O(n), 2min, 96s, 19mb
        if len(nums) <= 1:
            return False
        # visited = {}
        # for num in nums:
        #     if num in visited:
        #         return True
        #     else:
        #         visited[num] = 1
        # return False

        # NO2 reduce space to O(1), sort time O(nlogn), 17mb
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False



        
# @lc code=end

