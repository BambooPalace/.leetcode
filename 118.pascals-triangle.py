#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        # no 1 own, dp 7 mins, O(N^2) x 2
        # if numRows == 0:
        #     return []
        # dp = {}
        # dp[1] = [1]        
        # # append() is faster than += []
        # for i in range(2, numRows+1):
        #     dp[i] = [1]
        #     for j in range(1, i-1):
        #         dp[i] += [dp[i-1][j-1] + dp[i-1][j]]
        #     dp[i] += [1]        
        # return [v for v in dp.values()]
        # idea: symmetrical, may not need to add all
        
        # no2 rewrite using lists
        res = []
        if numRows == 0:
            return res
        res.append([1])
        if numRows == 1:            
            return res
        for i in range(1, numRows):
            res.append([1])
            for j in range(1, i):# bug1: range(1,i-1)
                res[i].append(res[i-1][j-1] + res[i-1][j])
            res[i].append(1)      
        return res

# @lc code=end

