#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # intuition, reminds me of threeSum, check solution straight
        
        # NO 1 Garvit, confusing solution, i hate backtracking...
        res = []
        def helper(candidates, target, curr, index):
            if target < 0:
                return
            if target == 0:
                res.append(curr)
                return
            # ???
            for start in range(index, len(candidates)):
                helper(candidates, target-candidates[start], curr+[candidates[start]], start)

        helper(candidates, target, [], 0)
        return res

        
# @lc code=end

