#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#

# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # done before, forget logic then remembered ! shift shorter bar
        
        n = len(height)
        l, r, res = 0, n-1, 0
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                # bug 1: easy bug affects my belief in the algo...
                r -= 1
        return res
                



        
# @lc code=end

