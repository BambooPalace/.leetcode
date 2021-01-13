#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # each number can be used once, but candidates can be duplicated
        # straight to Garvit solution, still CONFUSING...
        result = []
        candidates.sort()

        def recursive(candidates, target, currList, index):
        	if target < 0:
        		return
        	if target == 0:
        		result.append(currList)
        		return

        	previous = -1
        	for start in range(index, len(candidates)):
        		if previous != candidates[start]:
	        		recursive(candidates, target - candidates[start], currList + [candidates[start]], start+1)
	        		previous = candidates[start]


        recursive(candidates, target, [], 0)
        return result
# @lc code=end

