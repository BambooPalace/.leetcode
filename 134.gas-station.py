#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # own, think 5min, try code 12min, debug 10min
        # NO1 precheck NO case and then one pass, 36ms
        # if sum(cost) > sum(gas):
        #     return -1
        # i = 0
        # n = len(gas)
        # stock = 0        
        # res = 0
        # # bug 1: FAIL [5,8,2,8];[6,5,6,6]
        # while i < n:                        
        #     stock = max(0, stock + gas[i] - cost[i])
        #     if stock == 0:
        #         res = 0                
        #     elif stock > 0:
        #         if res == 0:
        #             res = i                
        #     i += 1
        # return res

        # own NO2 try modify to one pass, FAIL
        

        #NO3 Garvit, simpler code and logic, easy to avoid logic bugs
        start, curr_sum, total_sum =0, 0, 0
        for index in range(len(gas)):
            diff = gas[index] - cost[index]
            total_sum += diff
            curr_sum += diff # stock
            
            # below line is new to me, can write in alternative way also
            if curr_sum < 0: # return first idx of stock > 0
                start = index + 1
                curr_sum = 0
                
        if total_sum >= 0:
            return start
        return -1



        
# @lc code=end

