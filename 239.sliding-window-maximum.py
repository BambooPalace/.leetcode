#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # THIS IS INDEED HARD
        # no 1 brute force, O(N*K), TLE...
        # n = len(nums)
        # if k >= n:
        #     # note return type is list
        #     return [max(nums)]
        
        # res = []
        # for i in range(n - k + 1):
        #     # k operations
        #     res.append(max(nums[i:i+k]))            
        # return res

        # no 2, xiaohao deque, code NOT clear, TLE
        # n = len(nums)
        # if k >= n:
        #     # note return type is list
        #     return [max(nums)]
        # q = []
        # res = []
        # for i in range(n):
        #     while i and q and nums[i]>q[-1]:
        #         q = q[:-1]
        #     q.append(nums[i])
        #     if i>=k and nums[i-k]==q[0]:
        #         q = q[1:]
        #     if i >= k-1:
        #         res.append(q[0])
        # return res

        # no3, halfrost deque, TLE...
        # n = len(nums)
        # if k >= n:
        #     # note return type is list
        #     return [max(nums)]
        # q = []
        # res = []
        # for i, v in enumerate(nums):
        #     # if out of range, pop left
        #     if i >= k and q[0] <= i-k:
        #         q = q[1:]
        #     # if cur num larger than q right most element, pop right until not met condition
        #     while q and nums[q[-1]] < v:
        #         q = q[:-1]
        #     q.append(i)
        #     # add q[0] to res
        #     if i >= k-1:
        #         res.append(nums[q[0]])
        # return res

        # no4, Garvit, IMPORT DEQUE, operation faster
        n = len(nums)
        if k >= n:
            # note return type is list
            return [max(nums)]
        q = deque()
        # 1st q
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res = []
        for i in range(k, n):
            res.append(nums[q[0]])
            # pop out of range idx
            if q and q[0] <= i-k:
                q.popleft()
            # pop from right side if cur num larger than items in q
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res



        




# @lc code=end

