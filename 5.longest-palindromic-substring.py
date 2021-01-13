#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # known dp, try own，nah, check solution
        # no 1 Garvit, CANT understand code...
       

        #  CANT understand, just check video: NEETCODE, O(N*2)
        res = ''
        resLen = 0
        n = len(s)
        for i in range(n):
            # odd length
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            # EVEN length
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res

        
    



# @lc code=end

