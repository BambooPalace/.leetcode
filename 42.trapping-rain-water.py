#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # NO 1 cant think of, check video easy to understand
        # 48ms/46MS, 30% and 11%; O(3N), O(N)
        # n = len(height)
        # if n <= 2:
        #     return 0
        # res = 0
        # leftMax = [height[0]] * n
        # rightMax = [height[n-1]] * n
        # for i in range(1, n):
        #     leftMax[i] = max(height[i], leftMax[i-1])
        # for i in range(n-2, -1, -1):
        #     rightMax[i] = max(height[i], rightMax[i+1])        
        # for i in range(n):
        #     res += min(leftMax[i], rightMax[i]) - height[i]
        # return res

        # TRY: use leftMax = [0]*n, or sum(list) in last lines, time randome

        # halfrost, space O(1), O(N) , tricky
        n = len(height)
        if n <= 2:
            return 0
        res, left, right, maxLeft, maxRight = 0, 0, n-1, 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    res += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    res += maxRight - height[right]
                right -= 1
        return res
                





        
# @lc code=end

