#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # intuition: outside must be '()', ')' must be followed by extra '(' on the left
        # 7 min CANT think of code, check solution
        # res = []
        # l = r = 0 # track no of n '('')' left        
        # for n in range(2, n):

        # NO1 official sol , backtrack, tricky; O(4^N/sqrt(N))
        res = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        backtrack()
        return res

        # NO2 official sol, closure number, confusing DONT understand
        # if n == 0:
        #     return ['']
        # res = []
        # for c in range(n):
        #     for left in self.generateParenthesis(c):
        #         for right in self.generateParenthesis(n-1-c):
        #             res.append('('+left+')'+right)
        # return res

        # NO3 to check halfrost, seem same idea as no2 but easier to understand

        
# @lc code=end

