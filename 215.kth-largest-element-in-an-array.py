#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
import heapq

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # no 1 use sort()
        # nums = list(set(nums))    # wrong let, not distinct...read carefully    
        # nums.sort() # nlogn
        # return nums[-k]

        # no 2 xiaohao, heap        
        # return heapq.nlargest(k, nums)[-1]

        # no 3 based on xiaohao, failed, 
        # python heapq API not convenient, no peak kth level option, min heap only
        # h = [-nums[0]]
        # heapq.heapify(h)
        # for num in nums:
        #     if num > -h[0]:
        #         heapq.heappush(-num)
        # return 





        
# @lc code=end

