"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRoomsWRONG(self, intervals):
        # Write your code here
        # 1st draft 7 mins, O(nlogn), space = O(1); debug 4 mins
        # tricky, read questions carefully, its not same as counting overlapping intervals
        n = len(intervals)
        if n <= 1:
            return n
        intervals.sort(key=lambda x: x.start)
        previous = intervals[0]
        res = 1 # bug: start with at least 1 meeting room
        
        for i in range(1, n): #bug2: only check from 2nd interval
            if intervals[i].start > previous.end:
                previous = intervals[i]
            else:
                previous.end = max(previous.end, intervals[i].end)
                res += 1
        return res
        
# shanjingcheng youtube
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        # stores only end_time of rooms, min/earliest ending time is on 
        min_heap = [intervals[0].end]

        for i in range(1, len(intervals)):
            if interval[i].start < min_heap[0]:
                heapq.heappush(interval[i].end)
            else:
                heapq.heappushpop(interval[i].end)
        return len(min_heap)

    