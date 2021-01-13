#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # NO1 Garvit, backtrack
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [nums]
        res = []
        for i in range(n):
            for p in self.permute(nums[:i]+ nums[i+1:]):
                res.append([nums[i]] + p)
        return res
        

        
# @lc code=end

