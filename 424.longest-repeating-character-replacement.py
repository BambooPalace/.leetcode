#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # no 1 brute force
        n = len(s)
        if k >= n:
            return n
        # k is letter, v is list of distances
        map = {}
        for i, v in enumerate(s):
            if v in map:
                map[v].append(i - map[v][-1])
            else:
                map[v] = [i]
        # have no idea how to use the map

        
# @lc code=end

