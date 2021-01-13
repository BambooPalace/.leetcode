#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#
from math import ceil

# @lc code=start
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        # optional
        # if len(piles) == 1:
        #     return (piles[0] - 1) // H + 1

        def canFinish(k):
            # why (p-1)//k + 1 is correct and ceil(p/k) not right? test on command line ceil can work
            return sum([(p-1)//k + 1 for p in piles]) <= H
            # return sum([(ceil(p/k)) for p in piles]) <= H

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if canFinish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



    



        
# @lc code=end

