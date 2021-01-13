#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        k = len(p)
        res = []
        if not s or not k or n < k:
            return []
        # no 1 brute force, can not use set(p) as can be repeating
        # why test wrong? logic seem correct..spent many time, should check sol ealier
        #  get letter counter of p        
        counter = {}
        for c in p:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        temp = counter.copy()
        idx = []
        for i, v in enumerate(s[:n - k + 1]):
            # match counter with s
            if v in temp and temp[v] > 0:
                temp[v] -= 1
                idx.append(i)
            else:
                temp = counter.copy()
                idx = []
            # if counter fully matched, append 1st idx and empty idx list
            if sum(temp.values()) == 0:
                res.append(idx[0])
                idx = []
                # dont forget to reset counter
                temp = counter.copy()
        return res


            



# @lc code=end

