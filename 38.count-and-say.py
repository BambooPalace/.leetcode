#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # string problem, spent 30mins, give up for now
        # NO 1 own, idea 10min
        dp = {}
        dp[1] = '1'
        for i in range(2, n+1):
            count = {}
            # bug 2, 10 min only count multiple for continous num: "1211" => "111221" 
            # if so cannot use dictionary, as '1' is not unique
            for k, num in enumerate(dp[i-1]):
                if k > 0 and num == dp[i-1][k-1]:
                    count[num] += 1
                else:
                    count[num] = 1
            # bug 1, 10 min on this, note order
            dp[i] = ''
            for (key, val) in count.items():
                dp[i] = ''.join((str(val), key)) + dp[i]
        return dp[n]
        
# @lc code=end

