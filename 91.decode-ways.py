#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # NO1 try own, 10 mins nah, check solution      
        # n = len(s)
        # if n == 1:
        #     return 0 if s == '0' else 1
        # dp = {}
        # dp[1] = 1
        # num = int(s[:2])
        # dp[2] = 2 if num <= 26 and num % 10 > 0 else 1
        # dp[3]

        # NO 2 halfrost, roughly understand, not too clear
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            num = int(s[i-1:i])
            if num != 0:
                dp[i] = dp[i-1]
            num = int(s[i-2:i])
            if 10 <= num <= 26:
                dp[i] += dp[i-2]
        return dp[n]
            
        

        

# @lc code=end

