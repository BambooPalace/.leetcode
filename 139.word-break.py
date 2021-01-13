#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # NO1 own, 5 mins, FAIL "catsandog"; ["cats","dog","sand","and","cat"]
        # if len(wordDict) == 1 and s == wordDict[0]:
        #     return True
        # for word in wordDict:
        #     # not right, 
        #     if not s and s.startswith(word):
        #         l = len(word)
        #         s = s[l+1:]
        # return True if s else False

        # NO2 Garvit, roughly understand???        
        if len(wordDict) == 1 and s == wordDict[0]:
            return True
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[n]

        
# @lc code=end

