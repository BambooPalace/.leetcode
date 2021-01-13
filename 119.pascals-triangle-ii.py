#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # no1, based on 118
        # res = [[1]]
        # numRows = rowIndex + 1
        # if numRows == 1:            
        #     return res[-1]
        # for i in range(1, numRows):
        #     res.append([1])
        #     for j in range(1, i):# bug1: range(1,i-1)
        #         res[i].append(res[i-1][j-1] + res[i-1][j])
        #     res[i].append(1)      
        # return res[-1]

        # no 2 own, linear space, O(2N), troublesome...
        # last = [1]
        # numRows = rowIndex + 1
        # if numRows == 1:            
        #     return last
        # curr = last[:] #by value, not by refeerence
        # for i in range(1, numRows):
        #     last = curr[:]
        #     for j in range(1, i):
        #         curr[j] = last[j-1] + last[j]
        #     curr.append(1)     
        # return curr

        # NO 3 own idea, inplace and single temp value, can do but waste time
        # TIP from Garvit: UPDATE from right then NO NEED temp value
        # res = [1]
        # numRows = rowIndex + 1
        # if numRows == 1:            
        #     return res        
        # for i in range(1, numRows):
        #     temp = res[i//2]            
        #     for j in range(1, i):
        #         res[j] = res[j-1] + res[j]
        #     res.append(1)     
        # return res

        # no 4 Garvit, very simple and clean! NICE!
        row = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
        	for j in range(i-1, 0, -1):
        		row[j] += row[j-1]
        return row




# @lc code=end

