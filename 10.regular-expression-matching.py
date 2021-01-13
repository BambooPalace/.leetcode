#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
       
        # try own, brute force, 25mins CANT
         # HARD, should have checked sol earlier
        single = '.'
        wild = '*'
        i = j = 0
        m = len(s)
        n = len(p)
        while i < m and j < n:
            if s[i] != p[j] and if j!= n-1 and p[j+1]==wild:
                j += 2
            elif s[i] != p[j]:
                return False            
            elif p[j] == single:
                p[j] = s[i]
                i += 1
                j += 1
            elif p[j] == wild:
                if j == n-1:
                    break
                else:
                    if p[j+1] not in s[i:] and p[j+1] != single:
                        return False
                    if p[j+1] not in s[i:] and p[j+1] != single:
       
        return True
        # official solution...
        # forget about HARD for your practice

        
# @lc code=end

