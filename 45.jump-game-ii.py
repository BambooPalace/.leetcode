#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # own FAIL, think and code 17min, logic also not clear, TLE,
        # n = len(nums)
        # if n == 1:
        #     return 1
        # minJump = n
        # maxPos = 0
        # for i in range(n):
        #     maxPos = max(maxPos, i+nums[i])
        #     maxPos = min(maxPos, n-1)            
        #     minJump = min(minJump, 1 + self.jump(nums[maxPos:]))
        # return minJump

        # NO2 sol, Garvit, seem simple but I am CONFUSED...

        steps, lastRearch, maxReach = 0, 0 ,0

        for index in range(len(nums)):
        	if index > lastRearch:
        		lastRearch = maxReach
        		steps += 1
        	maxReach = max(maxReach, index + nums[index])

       	return steps
        
        
# @lc code=end

