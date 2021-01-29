#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # try and fail took so much time, next time if not confident see solution
        # NO1 try, brute, recursive, 26min FAIL max recursion depth...
        # if len(intervals) == 1:
        #     return intervals
        # res = [intervals[0]]  
        # overlap = False

        # for i in range(1, len(intervals)):
        #     left = intervals[i][0]
        #     right = intervals[i][1]
            
        #     for j, r in enumerate(res):
        #         # no overlapping
        #         if  left > r[1] or right < r[0]: # bug1: wrote 'and'
        #             if j == len(res) - 1:
        #                 res.append(intervals[i])
        #         else: # update the interval of the 1st overlapped list in res
        #             overlap = True
        #             if r[0] <= left <= r[1]:
        #                 r[1] = max(r[1], right)
        #             if r[0] <= right <= r[1]:
        #                 r[0] = min(r[0], left)
        #             break        

        # return res if not overlap else self.merge(res)

        #  NO2, halfrost, Sort and one pass, O(nlogn)
        intervals.sort() # defefault key is x[0]
        merged = []
        for interval in intervals:
            # after sorting the 1st element, no need to check right of interval
            # no need to check every merged interval also
            if not merged or merged[-1][1] < interval[0]: 
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        

                



        
# @lc code=end

