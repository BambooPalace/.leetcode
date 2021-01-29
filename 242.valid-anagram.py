#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # NO1 hashmap count, O(N), !space also O(N) as there r only 26 letters
        # 40ms
        # if len(s) != len(t):
        #     return False
        # # trick learned, no need two 
        # counter = {}
        # for i in range(len(s)):
        #     if s[i] not in counter:
        #         counter[s[i]] = 1
        #     else:
        #         counter[s[i]] += 1
        #     if t[i] not in counter:
        #         counter[t[i]] = -1
        #     else:                
        #         counter[t[i]] -= 1
        # # bug 1: logic wrong, -1 and 1 sums to 0...
        # ## return sum(counter.values()) == 0
        # for v in counter.values():
        #     if v != 0:
        #         return False
        # return True

        # NO2 official no1, sort and match, O(nlogn), O(1)
        # 48ms
        if len(s) != len(t):
            return False
        # bug1: string no sort() attribute
        s = list(s) # isnt new space after type changes?
        t = list(t)
        s.sort()
        t.sort()
        return s == t



        
# @lc code=end

