#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#

# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # CONFUSING, STILL hate backtracking
        # No 1, halfrost (Garvit no sol) code in GO so harder to understand
        # after I code it is WRONG  

        # NO2, leetcode DISCUSS, 640ms           
    #     res = []
    #     self.backtrack(n, k, res, [], 1)
    #     return res    
    # def backtrack(self, n, k, res, path, index):
    #     if len(path) == k:
    #         res.append(path)
    #         return
    #     for i in range(index, n+1):
    #         self.backtrack(n, k, res, path+[i], i+1)

    #     # NO3 dicuss, 152ms
    #     res = []
    #     self.dfs(range(1,n+1), k, [], res)
    #     return res        
    # def dfs(self, nums, k, path, res):
    #     if k == 0:
    #         res.append(path)
    #         return
    #     if len(nums) >= k:
    #         for i in range(len(nums)):
    #             self.dfs(nums[i+1:], k-1, path+[nums[i]], res)
    #     return

    #     # NO4 discuss, 92ms
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]
        
# @lc code=end

