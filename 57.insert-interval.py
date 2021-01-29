#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#

# @lc code=start
class Solution(object):
    def insert1(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # SPEND 30min do my own, another 30min just to understand others solutions TAT

        # NO1, own log(N) 88%: search insert idx, make new interval, merge inserted -1 portion 
        if not intervals:
            return [newInterval]
        # sorted and no duplicates, O(n)
        interval_starts = [interval[0] for interval in intervals]
        # binary search idx, O(logn)
        idx = self.searchInsertIndex(interval_starts, newInterval[0])
        intervals.insert(idx, newInterval)
        # merge, O(N) as NO NEED sort
        # bug 1: fail [[1,3],[6,9]]; [2,5]; merge need to back 1 index position
        idx = idx - 1 if idx > 0  else idx
        intervals[idx:] = self.merge(intervals[idx:])
        return intervals


    def searchInsertIndex(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def merge(self, intervals):
        # already sorted
        # intervals.sort() 
        merged = []
        for interval in intervals:
            # after sorting the 1st element, no need to check right of interval
            # no need to check every merged interval also
            if not merged or merged[-1][1] < interval[0]: 
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    # NO2 one pass, Garvit, tricky code hard to understand, could have checked video
    # O(N),  88%
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        res = []        
        for interval in intervals:
            if interval[1] < newInterval[0]: # section 1
                res.append(interval)
            # tricky to make complex conditions, brain power not enough...
            elif interval[0] > newInterval[1]: # section 3                
                res.append(newInterval)
                # TRICKY line, could have break into two loops
                newInterval = interval                                       

            else: # section 2, overlapped
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])        
        res.append(newInterval)
        return res

        # halfrost code in GO, not easy to see in a glance


        
# @lc code=end

